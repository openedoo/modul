from openedoo.core.libs import blueprint

modul_hello = blueprint('modul_hello', __name__)
@modul_hello.route('/', methods=['POST', 'GET'])
def index():
	return "Hello World"
