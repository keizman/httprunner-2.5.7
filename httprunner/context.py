from httprunner import parser, utils
from httprunner.loader.buildup import load_debugtalk_functions
from httprunner import exceptions


class SessionContext(object):
    """ HttpRunner session, store runtime variables.

    Examples:
        >>> variables = {"SECRET_KEY": "DebugTalk"}
        >>> context = SessionContext(variables)

        Equivalent to:
        >>> context = SessionContext()
        >>> context.update_session_variables(variables)

    """

    def __init__(self, variables=None, functions=None):
        variables_mapping = utils.ensure_mapping_format(variables or {})
        self.session_variables_mapping = parser.parse_variables_mapping(variables_mapping)
        self.test_variables_mapping = {}
        
        # Load functions from debugtalk.py if not provided
        if functions is None:
            try:
                self.functions_mapping = load_debugtalk_functions()
            except (ImportError, exceptions.FileNotFound):
                # debugtalk.py not found or import error, use empty functions
                self.functions_mapping = {}
        else:
            self.functions_mapping = functions
            
        self.init_test_variables()

    def init_test_variables(self, variables_mapping=None):
        """ init test variables, called when each test(api) starts.
            variables_mapping will be evaluated first.

        Args:
            variables_mapping (dict)
                {
                    "random": "${gen_random_string(5)}",
                    "authorization": "${gen_md5($TOKEN, $data, $random)}",
                    "data": '{"name": "user", "password": "123456"}',
                    "TOKEN": "debugtalk",
                }

        """
        variables_mapping = variables_mapping or {}
        variables_mapping = utils.ensure_mapping_format(variables_mapping)
        variables_mapping.update(self.session_variables_mapping)
        parsed_variables_mapping = parser.parse_variables_mapping(variables_mapping)

        self.test_variables_mapping = {}
        # priority: extracted variable > teststep variable
        self.test_variables_mapping.update(parsed_variables_mapping)
        self.test_variables_mapping.update(self.session_variables_mapping)

    def update_test_variables(self, variable_name, variable_value):
        """ update test variables, these variables are only valid in the current test.
        """
        self.test_variables_mapping[variable_name] = variable_value

    def update_session_variables(self, variables_mapping):
        """ update session with extracted variables mapping.
            these variables are valid in the whole running session.
        """
        variables_mapping = utils.ensure_mapping_format(variables_mapping)
        self.session_variables_mapping.update(variables_mapping)
        self.test_variables_mapping.update(self.session_variables_mapping)

    def eval_content(self, content):
        """ evaluate content recursively, take effect on each variable and function in content.
            content may be in any data structure, include dict, list, tuple, number, string, etc.
        """
        return parser.eval_lazy_data(content, self.test_variables_mapping, self.functions_mapping)
