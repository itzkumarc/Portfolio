import { describe, it, expect, beforeEach, vi } from 'vitest';

describe('Navigation Scroll Effect', () => {
  let nav;

  beforeEach(async () => {
    vi.resetModules();
    document.body.innerHTML = '<nav style="box-shadow: none;"></nav>';
    nav = document.querySelector('nav');

    // Mock pageYOffset
    Object.defineProperty(window, 'pageYOffset', {
      value: 0,
      writable: true,
      configurable: true
    });

    // Import main.js content directly to ensure it runs in this context
    // because top-level event listeners are added when the module is loaded.
    await import('./main.js');
  });

  it('should not have box shadow when scroll is exactly 100px', () => {
    window.pageYOffset = 100;
    window.dispatchEvent(new Event('scroll'));
    expect(nav.style.boxShadow).toBe('none');
  });

  it('should have box shadow when scroll is greater than 100px', () => {
    window.pageYOffset = 101;
    window.dispatchEvent(new Event('scroll'));
    expect(nav.style.boxShadow).toBe('0 4px 6px rgba(0, 0, 0, 0.3)');
  });

  it('should remove box shadow when scrolling back up to 100px or less', () => {
    // Scroll down first
    window.pageYOffset = 150;
    window.dispatchEvent(new Event('scroll'));
    expect(nav.style.boxShadow).toBe('0 4px 6px rgba(0, 0, 0, 0.3)');

    // Scroll up
    window.pageYOffset = 100;
    window.dispatchEvent(new Event('scroll'));
    expect(nav.style.boxShadow).toBe('none');
  });
});
