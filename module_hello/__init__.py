from openedoo.core.libs import blueprint

hello = blueprint('hello', __name__)

@hello.route('/', methods=['POST', 'GET'])
def index():
	return "Hello World"