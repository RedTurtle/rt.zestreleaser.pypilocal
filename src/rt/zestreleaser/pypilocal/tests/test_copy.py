# -*- coding: utf-8 -*-

import unittest
import mock
import tempfile

import rt.zestreleaser.pypilocal.pypi_local


context = {
    'tagdir': '/tmp/tha.example-0.1dev',
    'tag_already_exists': False,
    'version': '0.1dev',
    'workingdir': '/tmp/tha.example-svn',
    'name': 'tha.example',
    }


class CopyTest(unittest.TestCase):

    @mock.patch('rt.zestreleaser.pypilocal.pypi_local.get_destinations')
    @mock.patch('zest.releaser.utils.ask')
    def test_no_destination_should_be_noop(self, ask, choose):
        choose.return_value = None
        rt.zestreleaser.pypilocal.pypi_local.copy(context)
        self.assertFalse(ask.called)

    @mock.patch('rt.zestreleaser.pypilocal.pypi_local.get_destinations')
    @mock.patch('zest.releaser.utils.ask')
    @mock.patch('shutil.copy')
    @mock.patch('glob.glob')
    def test_call_copy(self, glob, shutil, ask, choose):
        tempdir = tempfile.mkdtemp()
        choose.return_value = [tempdir]
        ask.return_value = True
        glob.return_value = ['/tmp/tha.example-0.1dev/dist/tha.example-0.1dev.tar.gz']
        rt.zestreleaser.pypilocal.pypi_local.copy(context)
        shutil.assert_called_with(
            '/tmp/tha.example-0.1dev/dist/tha.example-0.1dev.tar.gz', tempdir)


class ConfigTest(unittest.TestCase):

    @mock.patch('os.path.expanduser')
    def test_returns_configparser(self, expanduser):
        tmpfile = tempfile.NamedTemporaryFile()
        expanduser.return_value = tmpfile.name
        tmpfile.write("""
[rt.zestreleaser.pypilocal]
tmp = /tmp/kkk
pypi-local = ../../pypi-local
""")
        tmpfile.flush()
        config = rt.zestreleaser.pypilocal.pypi_local.read_configuration(
            'mock')
        self.assertEqual('/tmp/kkk', config.get(
            'rt.zestreleaser.pypilocal', 'tmp'))

    def test_file_not_present_silently_ignores_it(self):
        config = rt.zestreleaser.pypilocal.pypi_local.read_configuration(
            'doesnotexist')
        self.assertEqual([], config.sections())


if __name__ == "__main__":
    unittest.main()
