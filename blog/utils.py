def check_read_articles(request):
    try:
        return request.session["read_articles"]
    except KeyError:
        request.session["read_articles"] = []
        return request.session["read_articles"]
