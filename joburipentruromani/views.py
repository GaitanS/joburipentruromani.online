from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.conf import settings
import os

@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow:",
        "",
        "Sitemap: https://joburipentruromani.online/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

@require_GET
def sitemap_xml(request):
    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://joburipentruromani.online/</loc>
        <lastmod>2025-03-17</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>"""
    return HttpResponse(sitemap_content, content_type="application/xml")
