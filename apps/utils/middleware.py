from django.utils.translation import activate
from django.http import HttpResponseRedirect


class SetLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang_header = request.headers.get('Accept-Language', 'us')
        lang_code = lang_header.split(',')[0].split('-')[0].strip()

        activate(lang_code)
        request.session['language'] = lang_code

        lang_url = request.path.split('/')[1]
        new_url = request.build_absolute_uri().replace(f'/{lang_url}/', f'/{lang_code}/')

        if lang_url != lang_code:
            return HttpResponseRedirect(new_url)

        response = self.get_response(request)
        return response


