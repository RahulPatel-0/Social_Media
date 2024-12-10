import os
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View

class ReactAppView(View):
    def get(self, request, *args, **kwargs):
        try:
            # Serve the React app's index.html
            with open(os.path.join(settings.REACT_BUILD_DIR, 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse(
                "React build files not found. Run 'npm run build' in your React project.",
                status=501,
            )
