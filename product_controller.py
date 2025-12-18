from constants import HttpStatus

from webob import Request, Response
from constants import inventory
from app import app


@app.route('/api/products')
def get_products(request: Request) -> Response:
    return Response(
        json_body=inventory,
    )


@app.route('/api/products/{category}')
def get_products_by_cat(request: Request, category: str) -> Response:
    if category not in inventory:
        return Response(
            json_body={
                "message": f"{category} doesn't exist in the inventory",
            },
            status=HttpStatus.NOT_FOUND,
        )
    return Response(
        json_body=inventory[category],
    )

# @app.route('/exception')
# def get_products(environ, start_response):
#     raise RuntimeError("just another exception")
