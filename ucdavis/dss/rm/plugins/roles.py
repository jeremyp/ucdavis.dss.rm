from AccessControl.SecurityInfo import ClassSecurityInfo
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin


class RolesPlugin(BasePlugin):
    """Determine the (global) roles which a user has.
    """
    security = ClassSecurityInfo()

    security.declarePrivate('getRoles ForPrincipal')
    def getRolesForPrincipal(self, principal, request=None):
        """principal -> (role_1, ... role_N)

        o Return a sequence of role names which the principal has.

        o May assign roles based on values in the REQUEST object, if present.
        """

        #add your code here

        pass

