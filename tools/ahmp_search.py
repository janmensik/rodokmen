#!/usr/bin/env python3
import sys, io, re, html, urllib.request, urllib.parse, http.cookiejar

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def search_ahmp(query, max_pages=10):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    B = "https://katalog.ahmp.cz"
    q = urllib.parse.quote_plus(query)
    
    url = f"{B}/pragapublica/searchlink?xid=7EF18906B65E11DF820F00166F1163D4&fcDb=&onlyDigi=&modeView=LIST&searchAsPhrase=&patternTxt={q}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 genealogy-research'})
    resp = opener.open(req)
    a_html = resp.read().decode('utf-8', 'replace')
    
    sp_m = re.search(r'name="_sourcePage" value="([^"]*)"', a_html)
    fp_m = re.search(r'name="__fp" value="([^"]*)"', a_html)
    if not sp_m or not fp_m:
        print("No results or failed to get form tokens.")
        return
        
    sp, fp = sp_m.group(1), fp_m.group(1)
    
    data = urllib.parse.urlencode({
        'pageRows': '51',
        'myPageRows': '',
        '_sourcePage': sp,
        '__fp': fp
    }).encode('utf-8')
    
    req_rows = urllib.request.Request(f"{B}/pragapublica/ViewControlImpl.action", data=data, headers={'User-Agent': 'Mozilla/5.0 genealogy-research'})
    cur_html = opener.open(req_rows).read().decode('utf-8', 'replace')
    
    def parse_page(t):
        items = []
        for blk in t.split('class="navigatorLine listArticle')[1:]:
            crumbs = re.findall(r'class="crumb">\s*<a[^>]*>([^<]*)</a>', blk)
            z = re.search(r'Zoomify.action\?xid=(\w+).*?%28(\d+)%29%29&amp;scanIndex=0" title="Zobrazit v plné kvalitě (\d+)', blk)
            lab = re.search(r'rowPg=\d+">(.*?)</a>', blk, re.S)
            l = re.sub(r'<[^>]+>', '', lab.group(1)) if lab else '?'
            z_info = f"XID: {z.group(1)}, scans: {z.group(3)}" if z else "-"
            txt = f"{html.unescape(l).strip()} | {crumbs[-1][:40] if crumbs else ''} | {z_info}"
            items.append(txt)
            print(txt)
        return items

    parse_page(cur_html)
    
    for k in range(1, max_pages):
        u_m = re.search(r'/pragapublica/PaginatorResult\.action[^"]*row=' + str(k*51), cur_html)
        if not u_m:
            break
        u = u_m.group(0).replace('&amp;', '&')
        req_p = urllib.request.Request(f"{B}{u}", headers={'User-Agent': 'Mozilla/5.0 genealogy-research'})
        cur_html = opener.open(req_p).read().decode('utf-8', 'replace')
        parse_page(cur_html)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_ahmp(sys.argv[1])
    else:
        print("Usage: python ahmp_search.py <query>")
