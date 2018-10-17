#!/usr/bin/env python

import sys
from time import sleep
from pjalib.uio import UIO
from optparse import OptionParser
from pjalib.pconfig import ConfigManager


class PBuildTemplateConfig(ConfigManager):
    """@brief Responsible for managing the icons dest client configuration."""

    SERVER      = "server"
    USERNAME    = "username"

    DEFAULT_CONFIG = {
        SERVER: "",
        USERNAME: "",
    }

    def __init__(self, uio, configFile):
        """@brief Constructor.
           @param uio UIO instance.
           @param configFile Config file instance."""
        super(PBuildTemplateConfig, self).__init__(uio, configFile, PBuildTemplateConfig.DEFAULT_CONFIG)

    def configure(self):
        """@brief configure the required parameters for normal opperation."""

        self.inputStr(PBuildTemplateConfig.SERVER, "Server address", False)

        self.inputStr(PBuildTemplateConfig.USERNAME, "Username", False)

        self.store()


class PBuildTemplateError(Exception):
    pass


class PBuildTemplate(object):
    """@brief Responsible for ???"""

    CONFIG_FILE = ".pbuildtemplate.cfg"

    def __init__(self, uio, options):
        """@brief Constructor
           @param uio A UIO instance object
           @param options The command line options object from OptionParser"""

        self._uio = uio
        self._options = options

        self._pBuildTemplateConfig = PBuildTemplateConfig(self._uio, PBuildTemplate.CONFIG_FILE)
        self._pBuildTemplateConfig.load()

    def run(self):
        """@brief """
        server = self._pBuildTemplateConfig.getAttr(PBuildTemplateConfig.SERVER)
        username = self._pBuildTemplateConfig.getAttr(PBuildTemplateConfig.USERNAME)

        incCount = 0
        while True:
            self._uio.info('PBuildTemplate (server=%s, username=%s) Running %d' % (server,username,incCount))
            sleep(1)
            incCount = incCount + 1

    def configure(self):
        """@brief configure the persisten attributes."""
        self._pBuildTemplateConfig.configure()

def main():
    """"@brief The program entry point. Your program must start from this function."""
    uio = UIO(syslogEnabled=True)

    opts = OptionParser(usage='This program does something, describe it here.')
    opts.add_option("--debug",  help="Enable debugging.", action="store_true", default=False)
    opts.add_option("--config", help="Configure the program.", action="store_true", default=False)
    opts.add_option("--host",   help="Followed by the host string argument.", default=None)
    opts.add_option("--int",    help="Followed by an integer value.", type="int", default=None)
    opts.add_option("--hint",   help="Followed by a hex integer value.", type="int", metavar="HEX", default=None)
    opts.add_option("--float",  help="Followed by a float value.", type="float", default=None)

    try:
        (options, args) = opts.parse_args()

        pBuildTemplate = PBuildTemplate(uio, options)

        if options.config:

            pBuildTemplate.configure()

        else:
            pBuildTemplate.run()

    # If the program throws a system exit exception
    except SystemExit:
        pass
    # Don't print error information if CTRL C pressed
    except KeyboardInterrupt:
        pass
    except:

        if options.debug:
            raise

        else:
            uio.error(sys.exc_value)


if __name__ == '__main__':
    main()
