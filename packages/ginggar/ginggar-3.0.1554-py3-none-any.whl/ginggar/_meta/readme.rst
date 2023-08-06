.. _h_firststeps:

===========
First Steps
===========

Please read how to make Ginggar ready for the first steps in :ref:`h_installation`.

The following steps require that all preparation steps are finished. In order to login, visit the Ginggar root url (e.g. :samp:`http://localhost:8000`) in your favorite browser and follow the instructions there.

Depending on your installation procedure, the initial admin user is directly preconfigured, so you can directly login and add some feeds.

What's Next?
============

Ginggar is a multi-user tool with an own user database.

User configuration must be made with the admin interface. You can create, remove and modify users (reset password, ...) there. The admin user can see it in the menu bar.

Create some users there for your friends/colleagues/clients. Give them your Ginggar url and the user data. Let them insert theirs favorite feeds and read the messages there.

Or simply use Ginggar with the admin account on a single-user machine :)

==================
How To Use Ginggar
==================

.. include:: UIREADME

.. _h_installation:

======================
Appendix: Installation
======================

Install Ginggar via the installation package for your environment, if a suitable one exists for download. This also takes care of installing dependencies and doing preparation (unless mentioned otherwise in the installation procedure). Use the source code archive as fallback. Please read more details about your installation flavour in the following.

.. rubric:: Installation on Debian

Just download the Ginggar package for Debian and install it. After the installation, the start menu contains a browser link to an automatically configured (apache2/wsgi-based) Ginggar site. Try the :ref:`h_firststeps`.

.. rubric:: Installation as Python wheel package

You need a Python environment with enabled 'wheel' functionality. Download the Ginggar wheel package and install it. Proceed with :ref:`h_setupginggar`.

.. rubric:: Installation From Source

Download the Ginggar source package and extract it to a destination. Install the :ref:`Dependencies <hhdependencies>` and proceed with :ref:`h_setupginggar` afterwards.

.. _h_setupginggar:

============================
Appendix: Setting Up Ginggar
============================

For some platforms, the installation automatically sets up a Ginggar service. If so, those are automatically enabled in background on some platforms and to be explicitly started by the user on other ones. The degree of service quality (in regards of performance, security, ...) can also differ between platforms. Read more about your scenario in :ref:`h_installation`.

If your installation package does automatically install a Ginggar service and you are fine with this one, you can skip this preparation step, ensure that the service is started, and proceed with :ref:`h_firststeps`.

Otherwise there are many options to set up a Ginggar service manually. The easiest way is to use the included personal Ginggar server (technically it uses the Django development server). Other ways are to let Ginggar run in a full web server. Please find out all existing possibilities in the Django documentation. Real web servers typically provide much higher service quality.

The first step for any installation way is to run the Ginggar admin tool. Open a terminal window. You need to have write permissions for the Ginggar installation directory for the following steps.

*Finding ginggar_admin:* Now you have to find out the path to :file:`ginggar_admin`. For some platforms, the name can be used directly, but on other ones (e.g. if you use the source package) you have to find it somewhere in the Ginggar installation directory; typically in :file:`.../_meta/misc/ginggar_admin.py` or likewise.

Call this tool this way for setting up a brand new Ginggar installation:

.. code-block:: sh

  ginggar_admin setup "/home/foo/.ginggar"

The second parameter specifies a storage location for Ginggar runtime data like the database files.

Afterwards you can start the included personal server this way and browse to the printed destination:

.. code-block:: sh

  ginggar_admin runserver

This way you could - at least for the moment - proceed with :ref:`h_firststeps`.

For public servers you have to run Ginggar in a real web server.

The following gives some short hints for installing Ginggar in Apache 2.4 with :samp:`mod_wsgi`. If you plan to use a different software stack, you should also read the Django documentation. You probably need certain write permissions during the process.

*Finding the local settings file:* Find the file :file:`settings_local.py`, which is typically stored in the Ginggar installation directory or in its :file:`ginggar` subdirectory after you set up Ginggar.

The :file:`settings_local.py` must be adapted. Adapt the following settings, but don't remove unlisted ones; just ignore them!:

.. code-block:: python

  DEBUG = False  # at least when everything works
  DATABASES = ...  # as it was or with another database
  STATIC_ROOT = "/var/lib/ginggar/static/"  # used for static files
  ...

Afterwards, run this on a terminal:

.. code-block:: sh

  ginggar_admin init

Embed Ginggar as wsgi application into an Apache2. Use :file:`_meta/misc/apache2.conf` and :file:`_meta/misc/ginggar.wsgi` for inspiration.

If you are more comfortable with a different approach to hosting Django applications, find the application in the Ginggar installation directory and host it like a typical Django application without doing any :samp:`ginggar_admin` calls!

==========================
Appendix: Single User Mode
==========================

Ginggar can optionally be operated in single user mode without login. It will use the factory default admin account internally and does not provide multi user and authentication functionality anymore.

Add the following line to your :file:`ginggar/settings_local.py`:

.. code-block:: python

  SINGLE_USER_MODE = True

========================
Appendix: User Scripting
========================

Users are allowed to add custom scripts in the *Settings* dialog. However, for security reasons, backend side scripts are only available to users on a whitelist. This is automatically true in single user mode. Otherwise, set a global configuration with key `allowuserscriptingfor` to a json serialized list of user names for setting up this whitelist.

=================================
Appendix: External Authentication
=================================

Ginggar can use an external authentication method instead of the internal user database. Write an executable (e.g. a shell script) with the following behavior:

- Read one line from stdin: this is a user name
- Read one line from stdin: this is the password
- Check that for correctness and print the username if and only if login data are correct
- Terminate

The returned username should be a modified version of the given one if it may contain problematic characters (like :samp:`@`, :samp:`%`, ...). The easiest solution is to just remove them. The executable must be allowed to be executed by the web server.

Add a line like this in your :file:`ginggar/settings_local.py`:

.. code-block:: python

  EXTERNAL_AUTH_HELPER = '/path/to/your/auth_helper'

Note that the admin interface will still use the internal database! Since you don't need it in this case, you should hide it in your server configuration or at least reset the default admin password!

===============================================
Appendix: Manually Updating The Database Scheme
===============================================

For installations without a package manager, you have to manually update the database scheme whenever a new version brings some changes in the Ginggar data storage structures. Update the source code first and then call this command:

.. code-block:: sh

  ginggar_admin update
