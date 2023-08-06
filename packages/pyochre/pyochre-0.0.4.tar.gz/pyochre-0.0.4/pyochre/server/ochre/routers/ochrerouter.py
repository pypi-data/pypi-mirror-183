from rest_framework.routers import Route, DynamicRoute
from rest_framework_nested.routers import DefaultRouter


class OchreRouter(DefaultRouter):
    def __init__(self, *argv, **argd):
        retval = super(OchreRouter, self).__init__(self, *argv, **argd)
        return retval

    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={
                "get": 'list',
                "post" : "create"
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={
                "get": "retrieve",
                "put" : "update",
                "patch" : "partial_update",
                "delete" : "destroy"
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        DynamicRoute(
            url=r'^{prefix}/{url_path}/{lookup}/$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        ),
        DynamicRoute(
            url=r'^{prefix}/{url_path}/$',
            name='{basename}-{url_name}',
            detail=False,
            initkwargs={}
        )
    ]

