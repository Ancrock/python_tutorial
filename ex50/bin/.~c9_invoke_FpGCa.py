import web

urls = (
	'/', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
	def GET(self):
		greeting = "Hello World"
		return greet

if __name__ == "__main__":
	app.run()