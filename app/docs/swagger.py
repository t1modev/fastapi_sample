from fastapi.openapi.utils import get_openapi

def setup_swagger(app):
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="Test API",
            version="0.0.1",
            description="API Documentation",
            routes=app.routes,
        )
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi