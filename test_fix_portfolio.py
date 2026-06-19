import re
from fix_portfolio import apply_fixes

def test_apply_fixes_mobile_nav():
    content = "Before <!-- Mobile Bottom Navigation --> Old Nav <!-- Main Content --> After"
    result = apply_fixes(content)
    assert "Before" in result
    assert "After" in result
    assert "<!-- Mobile Bottom Navigation -->" in result
    assert "<!-- Main Content -->" in result
    assert "Pubs" in result
    assert "Conf" in result
    assert "Old Nav" not in result

def test_apply_fixes_duplicate_section():
    content = '<section id="conferences" class="content-section">  <section id="conferences" class="content-section">'
    result = apply_fixes(content)
    assert result == '<section id="conferences" class="content-section">'

def test_apply_fixes_duplicate_section_with_newline():
    content = '<section id="conferences" class="content-section">\n<section id="conferences" class="content-section">'
    result = apply_fixes(content)
    assert result == '<section id="conferences" class="content-section">'

def test_apply_fixes_no_change():
    content = "This content should not change."
    result = apply_fixes(content)
    assert result == content
