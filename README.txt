To build the package

- Ensure the python-pbuild package is installed.
- Run 'sudo pbuild' in this folder.

The packages folder should then contain the Linux packages (deb, rpm and tgz)


Required folders

python
Contains the python files to be included in the installation.
Any python files in this folder must have a main function (def main())
as the program entry point. The filename will then become the command 
available on the system (E.G doitnow.py means the doitnow command will
be available after the installation). 
This folder may also contain other folders that contain python 
modules (__init__.py present in folder). After installation these
folders will be available for import by the above programs and 
any other programs on the system (I.E they can be used as libraries).

debian
This contains the debian files that control the package installation.
This is typically control, postinst, postrm, preinst, prerm
See https://www.debian.org/doc/manuals/debian-faq/ch-pkg_basics.en.html 
for more information on this.


Optional folder

init.d
If this folder is present it should contain the startup scripts that 
sit in the /etc/init.d folder that auto starts programs on system 
powerup.
