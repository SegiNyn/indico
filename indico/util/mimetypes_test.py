# This file is part of Indico.
# Copyright (C) 2002 - 2022 CERN
#
# Indico is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see the
# LICENSE file for more details.

import pytest

from indico.util.mimetypes import icon_from_mimetype


@pytest.mark.parametrize(('mimetype', 'expected_icon'), (
    ('application/applixware', 'default_icon'),
    ('application/atom+xml', 'icon-file-xml'),
    ('application/cdmi-capability', 'default_icon'),
    ('application/dssc+der', 'default_icon'),
    ('application/ecmascript', 'default_icon'),
    ('application/json', 'icon-file-css'),
    ('application/msword', 'icon-file-word'),
    ('application/pdf', 'icon-file-pdf'),
    ('application/prs.cww', 'default_icon'),
    ('application/relax-ng-compact-syntax', 'default_icon'),
    ('application/resource-lists+xml', 'icon-file-xml'),
    ('application/vnd.3gpp.pic-bw-large', 'default_icon'),
    ('application/vnd.openofficeorg.extension', 'default_icon'),
    ('application/vnd.openxmlformats-officedocument.presentationml.presentation', 'icon-file-presentation'),
    ('application/vnd.openxmlformats-officedocument.presentationml.slide', 'default_icon'),
    ('application/vnd.openxmlformats-officedocument.presentationml.slideshow', 'default_icon'),
    ('application/vnd.openxmlformats-officedocument.presentationml.template', 'default_icon'),
    ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'icon-file-excel'),
    ('application/vnd.openxmlformats-officedocument.spreadsheetml.template', 'default_icon'),
    ('application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'icon-file-word'),
    ('application/vnd.openxmlformats-officedocument.wordprocessingml.template', 'default_icon'),
    ('application/vnd.oasis.opendocument.chart', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.chart', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.chart-template', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.database', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.formula', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.formula-template', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.graphics', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.graphics-template', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.image', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.image-template', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.presentation', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.presentation-template', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.spreadsheet', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.spreadsheet-template', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.text', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.text-master', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.text-template', 'icon-file-openoffice'),
    ('application/vnd.oasis.opendocument.text-web', 'icon-file-openoffice'),
    ('application/vnd.ms-artgalry', 'default_icon'),
    ('application/vnd.ms-cab-compressed', 'default_icon'),
    ('application/vnd.ms-excel', 'icon-file-excel'),
    ('application/vnd.ms-excel.addin.macroenabled.12', 'default_icon'),
    ('application/vnd.ms-excel.sheet.binary.macroenabled.12', 'default_icon'),
    ('application/vnd.ms-excel.sheet.macroenabled.12', 'default_icon'),
    ('application/vnd.ms-excel.template.macroenabled.12', 'default_icon'),
    ('application/vnd.ms-fontobject', 'default_icon'),
    ('application/vnd.ms-htmlhelp', 'default_icon'),
    ('application/vnd.ms-ims', 'default_icon'),
    ('application/vnd.ms-lrm', 'default_icon'),
    ('application/vnd.ms-officetheme', 'default_icon'),
    ('application/vnd.ms-pki.seccat', 'default_icon'),
    ('application/vnd.ms-pki.stl', 'default_icon'),
    ('application/vnd.ms-powerpoint', 'icon-file-presentation'),
    ('application/vnd.ms-powerpoint.addin.macroenabled.12', 'default_icon'),
    ('application/vnd.ms-powerpoint.presentation.macroenabled.12', 'default_icon'),
    ('application/vnd.ms-powerpoint.slide.macroenabled.12', 'default_icon'),
    ('application/vnd.ms-powerpoint.slideshow.macroenabled.12', 'default_icon'),
    ('application/vnd.ms-powerpoint.template.macroenabled.12', 'default_icon'),
    ('application/vnd.ms-project', 'default_icon'),
    ('application/vnd.ms-word.document.macroenabled.12', 'default_icon'),
    ('application/vnd.ms-word.template.macroenabled.12', 'default_icon'),
    ('application/vnd.ms-works', 'default_icon'),
    ('application/vnd.ms-wpl', 'default_icon'),
    ('application/vnd.ms-xpsdocument', 'default_icon'),
    ('application/vnd.zzazz.deck+xml', 'icon-file-xml'),
    ('application/x-7z-compressed', 'icon-file-zip'),
    ('application/x-ace-compressed', 'icon-file-zip'),
    ('application/x-bzip', 'icon-file-zip'),
    ('application/x-bzip2', 'icon-file-zip'),
    ('application/x-dtbncx+xml', 'icon-file-xml'),
    ('application/xhtml+xml', 'icon-file-xml'),
    ('application/xml', 'icon-file-xml'),
    ('application/zip', 'icon-file-zip'),
    ('audio/adpcm', 'icon-file-music'),
    ('audio/basic', 'icon-file-music'),
    ('audio/midi', 'icon-file-music'),
    ('audio/mp4', 'icon-file-music'),
    ('audio/mpeg', 'icon-file-music'),
    ('audio/ogg', 'icon-file-music'),
    ('audio/vnd.dece.audio', 'icon-file-music'),
    ('audio/vnd.digital-winds', 'icon-file-music'),
    ('audio/x-aac', 'icon-file-music'),
    ('chemical/x-cdx', 'default_icon'),
    ('image/bmp', 'icon-file-image'),
    ('image/cgm', 'icon-file-image'),
    ('image/g3fax', 'icon-file-image'),
    ('image/gif', 'icon-file-image'),
    ('image/ief', 'icon-file-image'),
    ('image/jpeg', 'icon-file-image'),
    ('image/ktx', 'icon-file-image'),
    ('image/png', 'icon-file-image'),
    ('image/prs.btif', 'icon-file-image'),
    ('image/svg+xml', 'icon-file-image'),
    ('image/tiff', 'icon-file-image'),
    ('image/vnd.adobe.photoshop', 'icon-file-image'),
    ('image/vnd.dece.graphic', 'icon-file-image'),
    ('image/vnd.dvb.subtitle', 'icon-file-image'),
    ('image/vnd.djvu', 'icon-file-image'),
    ('image/vnd.dwg', 'icon-file-image'),
    ('image/vnd.dxf', 'icon-file-image'),
    ('image/vnd.fastbidsheet', 'icon-file-image'),
    ('image/vnd.fpx', 'icon-file-image'),
    ('image/vnd.fst', 'icon-file-image'),
    ('image/vnd.fujixerox.edmics-mmr', 'icon-file-image'),
    ('image/vnd.fujixerox.edmics-rlc', 'icon-file-image'),
    ('image/vnd.ms-modi', 'icon-file-image'),
    ('image/vnd.net-fpx', 'icon-file-image'),
    ('image/vnd.wap.wbmp', 'icon-file-image'),
    ('image/vnd.xiff', 'icon-file-image'),
    ('image/webp', 'icon-file-image'),
    ('image/x-cmu-raster', 'icon-file-image'),
    ('image/x-cmx', 'icon-file-image'),
    ('image/x-freehand', 'icon-file-image'),
    ('image/x-icon', 'icon-file-image'),
    ('image/x-pcx', 'icon-file-image'),
    ('image/x-pict', 'icon-file-image'),
    ('image/x-portable-anymap', 'icon-file-image'),
    ('image/x-portable-bitmap', 'icon-file-image'),
    ('image/x-portable-graymap', 'icon-file-image'),
    ('image/x-portable-pixmap', 'icon-file-image'),
    ('image/x-rgb', 'icon-file-image'),
    ('image/x-xbitmap', 'icon-file-image'),
    ('image/x-xpixmap', 'icon-file-image'),
    ('image/x-xwindowdump', 'icon-file-image'),
    ('text/calendar', 'icon-calendar'),
    ('text/css', 'icon-file-css'),
    ('text/csv', 'icon-file-spreadsheet'),
    ('text/html', 'icon-file-xml'),
    ('text/n3', 'icon-file-xml'),
    ('text/plain', 'icon-file-text'),
    ('text/plain-bas', 'icon-file-text'),
    ('text/prs.lines.tag', 'icon-file-text'),
    ('text/richtext', 'icon-file-text'),
    ('text/sgml', 'icon-file-xml'),
    ('text/tab-separated-values', 'icon-file-spreadsheet'),
    ('video/h264', 'icon-file-video'),
    ('video/jpeg', 'icon-file-video'),
    ('video/jpm', 'icon-file-video'),
    ('video/mj2', 'icon-file-video'),
    ('video/mp4', 'icon-file-video'),
    ('video/mpeg', 'icon-file-video'),
    ('video/ogg', 'icon-file-video'),
    ('video/quicktime', 'icon-file-video'),
    ('video/vnd.dece.hd', 'icon-file-video'),
    ('video/vnd.dece.mobile', 'icon-file-video'),
    ('video/x-f4v', 'icon-file-video'),
    ('video/x-fli', 'icon-file-video'),
    ('video/x-flv', 'icon-file-video'),
    ('video/x-m4v', 'icon-file-video'),
    ('video/x-ms-asf', 'icon-file-video'),
    ('video/x-ms-wm', 'icon-file-video'),
    ('video/x-ms-wmv', 'icon-file-video'),
    ('video/x-ms-wmx', 'icon-file-video'),
    ('video/x-ms-wvx', 'icon-file-video'),
    ('video/x-msvideo', 'icon-file-video'),
    ('video/x-sgi-movie', 'icon-file-video'),
    ('x-conference/x-cooltalk', 'default_icon')
))
def test_icon_from_mimetype(mimetype, expected_icon):
    assert icon_from_mimetype(mimetype, default_icon='default_icon') == expected_icon


def test_icon_from_mimetype_case_insensitive():
    assert icon_from_mimetype('IMAGE/gif', default_icon='default_icon') == 'icon-file-image'
