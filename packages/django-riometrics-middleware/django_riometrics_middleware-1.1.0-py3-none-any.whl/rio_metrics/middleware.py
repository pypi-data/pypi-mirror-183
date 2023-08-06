import os
import time

from rio_metrics.collector import HTTPMetricsCollector, IOMetricsProtocol

IO_METRICS_HOST = os.environ.get('IO_METRICS_HOST', 'localhost')
IO_METRICS_UDP_PORT = int(os.environ.get('IO_METRICS_UDP_PORT', '8092'))
IO_METRICS_HTTP_PORT = int(os.environ.get('IO_METRICS_HTTP_PORT', '8093'))
IO_METRICS_PROTOCOL = os.environ.get('IO_METRICS_PROTOCOL', 'udp')


class HTTPMetricsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        port = IO_METRICS_UDP_PORT
        if IO_METRICS_PROTOCOL == IOMetricsProtocol.HTTP.value:
            port = IO_METRICS_HTTP_PORT
        self.collector = HTTPMetricsCollector(IO_METRICS_PROTOCOL, IO_METRICS_HOST, port)

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        route, path_params = self._get_route_and_path_params(request)

        self.collector.collect(duration=time.time() - start_time,
                               method=request.method, route=route,
                               path_params=path_params,
                               code=response.status_code)

        return response

    @staticmethod
    def _get_route_and_path_params(request):
        route = '<unnamed route>'
        params = {}

        if hasattr(request, 'resolver_match'):
            if request.resolver_match is not None:
                if request.resolver_match.route is not None:
                    route = request.resolver_match.route
                if request.resolver_match.kwargs is not None:
                    params = request.resolver_match.kwargs

        return route, params
