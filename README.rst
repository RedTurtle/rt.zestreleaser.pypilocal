Introduction
============

This is a plugin for `zest.releaser`__ for being able to automatically copy releases of your products
to a local directory.

__ http://pypi.python.org/pypi/zest.releaser

This can be useful in some special customer environments, for example behind strong firewall and network
policies, where reaching an external pypi repository is not simple.

How to use
==========

You must configure your ``~/.pypirc`` file, adding to it a configuration like the one that follow::

    [rt.zestreleaser.pypilocal]
    pypi-local = ../../pypi-local

In this example next time you will run the ``fullrelease`` utility, a folder named ``pypi-local`` will be
searched two level above the current working directory.

In a common *buildout* environment this is a normal situation::

    buildout-directory
             |
            ...
             |_ pypi-local
            ...
              \_ src
                  |
                 ...
                   \_ your.package

It this way the ``pypi-local`` folder will be looked in the buildout directory root.

You can also provide multiple path, or system absolute paths::

    [rt.zestreleaser.pypilocal]
    pypi-local = ../../pypi-local
    global = /opt/global-pypi

For every found match, ``zest.releaser`` will ask to you if copy the release in the folder::

    ....
    Register and upload to pypi (y/N)?
    Register and upload to plone.org (Y/n)? n
    Copy egg to folder /Users/keul/buildout/test/pypi-local (Y/n)? Y
    Copy egg to folder /opt/global-pypi (Y/n)?

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
