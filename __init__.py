from openedoo.core.libs import blueprint

module_hello = blueprint('modul_hello', __name__)
@module_hello.route('/', methods=['POST', 'GET'])
def index():
	return "Hello World"
