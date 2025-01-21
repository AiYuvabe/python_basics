async def app(scope, receive, send):
    # HTTP response headers
    headers = [('Content-Type', 'text/html; charset=utf-8')]

    # Start the HTTP response
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/html'],
        ],
    })

    await send({
        'type': 'http.response.body',
        'body': b'Hii!',
    })
    
    