import os
import sys
import contextlib
import subprocess
import itertools
import functools
import argparse
import pathlib
import types
import importlib

import packaging.requirements

try:
    from importlib import metadata  # type: ignore
except ImportError:
    import importlib_metadata as metadata  # type: ignore

from ._py38compat import subprocess_path as sp


class Install(types.SimpleNamespace):

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-r',
        '--requirement',
        action='append',
        type=pathlib.Path,
        default=[],
    )
    parser.add_argument('package', nargs='*')

    @classmethod
    def parse(cls, args):
        parsed, unused = cls.parser.parse_known_args(args)
        return cls(**vars(parsed))

    def __bool__(self):
        """
        Return True only if the args to pip install
        indicate something to install.

        >>> bool(Install.parse(['inflect']))
        True
        >>> bool(Install.parse(['-q']))
        False
        >>> bool(Install.parse(['-q', 'inflect']))
        True
        >>> bool(Install.parse(['-rfoo.txt']))
        True
        >>> bool(Install.parse(['projects/inflect']))
        True
        >>> bool(Install.parse(['~/projects/inflect']))
        True
        """
        return bool(self.requirement or self.package)


def target_mod():
    mode = os.environ.get('PIP_RUN_MODE', 'ephemeral')
    return importlib.import_module(f'.{mode}', package=__package__)


def empty(path):
    return not bool(list(path.iterdir()))


@contextlib.contextmanager
def load(*args):
    with target_mod().context(args) as target:
        cmd = (sys.executable, '-m', 'pip', 'install', '-t', sp(target)) + args
        env = dict(os.environ, PIP_QUIET="1")
        Install.parse(args) and empty(target) and subprocess.check_call(cmd, env=env)
        yield str(target)


@contextlib.contextmanager
def _save_file(filename):
    """
    Capture the state of filename and restore it after the context
    exits.
    """
    # For now, only supports a missing filename.
    if os.path.exists(filename):
        tmpl = "Unsupported with extant {filename}"
        raise NotImplementedError(tmpl.format(**locals()))
    try:
        yield
    finally:
        if os.path.exists(filename):
            os.remove(filename)


# from jaraco.context
class suppress(contextlib.suppress, contextlib.ContextDecorator):
    """
    A version of contextlib.suppress with decorator support.

    >>> @suppress(KeyError)
    ... def key_error():
    ...     {}['']
    >>> key_error()
    """


def with_prereleases(spec):
    """
    Allow prereleases to satisfy the spec.
    """
    spec.prereleases = True
    return spec


@suppress(
    packaging.requirements.InvalidRequirement,
    metadata.PackageNotFoundError,  # type: ignore
)
def pkg_installed(spec):
    req = packaging.requirements.Requirement(spec)
    return metadata.version(req.name) in with_prereleases(req.specifier)


not_installed = functools.partial(itertools.filterfalse, pkg_installed)
