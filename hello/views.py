import textwrap

from django.http import HttpResponse
from django.views.generic.base import View



class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Constitution API</title>
            </head>
            <body>
                <h1>Constitution API</h1>
                <p>This site is currently in development. When finished, it will serve as an API for data relating to the U.S. Constitution.</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)


