import webbrowser

query = input("Co chces hledat?: ")
#moje url
def vyskakovac_oken(query):
    url_list = [f"https://www.google.com/?gws_rd=cr,ssl&ei=NCZFWIOJN8yMsgHCyLV4&fg=1#q={query}",
                f"https://www.google.com/?gws_rd=cr,ssl&ei=NCZFWIOJN8yMsgHCyLV4&fg=1#q={query}",
                f"https://twitter.com/search?q=%23{query}&src=typeahead_click",
                f"https://www.youtube.com/results?search_query={query}",
                f"https://www.facebook.com/search/pages/?q={query}&epa=SEARCH_BOX",
                f"https://www.reddit.com/r/{query}/"
               ]
    #reseni u wikipedie
    if " " in query:
        nove_query = "_".join(query.split())
        url_wikipedie = f"https://cs.wikipedia.org/wiki/{nove_query}"
        url_list.append(url_wikipedie)
    else:
        url_wikipedie = f"https://cs.wikipedia.org/wiki/{query}"
        url_list.append(url_wikipedie)
    for url in url_list:
      #otevreni stranek

      webbrowser.open_new(url)
vyskakovac_oken(query)

