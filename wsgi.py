def application(environ, start_response):
    start_response('301 Permanent Redirect', [
        ('Content-Type', 'text/html'),
        ('Location', 'https://openplans.org' + environ['PATH_INFO'])
    ])

    return [
        '<html>'
        '<head>'
            '<title>Plan in a Box</title>'
        '</head>'
        '<body>'
            'Plan in a Box is now <a href="https://openplans.org/">OpenPlans</a>.'
            'Please update your records accordingly.'
        '</body>'
        '</html>'
    ]
