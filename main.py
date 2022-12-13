from aiohttp import web
import datetime

routes = web.RouteTableDef()

@routes.get('/')
def index(request: web.Request):
    return web.Response(body='<html><body><h1>'+str(datetime.datetime.now())+'</h1></body></html>', content_type='text/html', headers={'Refresh': '0'})

if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host='127.0.0.1', port=8765)
