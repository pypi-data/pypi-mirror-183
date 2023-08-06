#include <cstdint>
#include <cstring>
#include <limits.h>
#include <math.h>
#include <cstdlib>
#include <iostream>

#define CMASK 0x00FFFFFF

#define RMASK 0x00FF0000
#define GMASK 0x0000FF00
#define BMASK 0x000000FF
#define AMASK 0xFF000000

#define RBMSK 0x00FF00FF
#define AGMSK 0xFF00FF00
#define AONE 0x01000000

/***********************************************************************************************************************

PIXEL FUNCTIONS

***********************************************************************************************************************/

inline void setPixel(size_t _pixels, int width, int height, int x, int y, size_t color, bool blending = false) {
    if ((unsigned) x < (unsigned) width && (unsigned) y < (unsigned) height) {
        uint32_t c = (uint32_t) color, i = y * width + x;
        uint32_t* p = (uint32_t*) _pixels;

        if (blending && p[i] & AMASK) {
            uint8_t a = c >> 24, na = ~a;
            uint32_t rb = (na * (p[i] & RBMSK) + a * (c & RBMSK)) >> 8;
            uint32_t ag = na * ((p[i] & AGMSK) >> 8) + a * (AONE | (c & GMASK) >> 8);
            p[i] = (rb & RBMSK) | (ag & AGMSK);
        } else p[i] = c;
    }
}

inline int getPixel(size_t _pixels, int width, int height, int x, int y) {
    if (x < width && y < height && x >= 0 && y >= 0) {
        return (int) ((uint32_t*) _pixels)[y * width + x];
    }
    return 0;
}

/***********************************************************************************************************************

BUFFER FUNCTIONS

***********************************************************************************************************************/

inline size_t createPixelBuffer(int width, int height) {
    return (size_t) calloc(width * height, sizeof(uint32_t));
}

inline void freePixelBuffer(size_t buffer) {
    free((void*) buffer);
}

inline void clearPixels(size_t _pixels, int width, int height) {
    memset((size_t*) _pixels, 0, width * height * sizeof(uint32_t));
}

inline size_t clonePixelBuffer(size_t _source, int width, int height) {
    size_t size = width * height * sizeof(uint32_t);
    return (size_t) memcpy(malloc(size), (void*) _source, size);
}

inline void blit(size_t _source, size_t _destination, int sw, int sh, int dw, int dh, int srx, int sry, int srw, int srh, int drx, int dry, int drw, int drh) {
    for (int y = 0; y < srh; y++) {
        for (int x = 0; x < srw; x++) {
            if (x < drw && y < drh) {
                setPixel(_destination, dw, dh, drx + x, dry + y, getPixel(_source, sw, sh, srx + x, sry + y), true);
            }
        }
    }
}

inline void colorkeyCopy(size_t source, size_t destination, int width, int height, size_t color_key) {
    uint32_t* source_buffer = (uint32_t*) source;
    uint32_t* destination_buffer = (uint32_t*) destination;
    for (int i = 0; i < width * height; i++) {
        if (source_buffer[i] != color_key) {
            destination_buffer[i] = source_buffer[i];
        } else {
            destination_buffer[i] = 0;
        }
    }
}

inline void switchColors(size_t _pixels, int width, int height, size_t color1, size_t color2) {
    uint32_t* pixels = (uint32_t*) _pixels;
    for (int i = 0; i < width * height; i++) {
        if (pixels[i] == color1) {
            pixels[i] = color2;
        }
    }
}

inline void flipX(size_t _pixels, int width, int height) {
    uint32_t* pixels = (uint32_t*) _pixels;
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width / 2; x++) {
            uint32_t temp = pixels[y * width + x];
            pixels[y * width + x] = pixels[y * width + width - x - 1];
            pixels[y * width + width - x - 1] = temp;
        }
    }
}

inline void flipY(size_t _pixels, int width, int height) {
    uint32_t* pixels = (uint32_t*) _pixels;
    for (int y = 0; y < height / 2; y++) {
        for (int x = 0; x < width; x++) {
            uint32_t temp = pixels[y * width + x];
            pixels[y * width + x] = pixels[(height - y - 1) * width + x];
            pixels[(height - y - 1) * width + x] = temp;
        }
    }
}

inline void flipAntiDiagonal(size_t _pixels, int width, int height) {
    uint32_t* pixels = (uint32_t*) _pixels;
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            if (x < y) {
                uint32_t temp = pixels[y * width + x];
                pixels[y * width + x] = pixels[x * width + y];
                pixels[x * width + y] = temp;
            }
        }
    }
}

/***********************************************************************************************************************

LINE FUNCTIONS

***********************************************************************************************************************/

inline void _drawLine(size_t _pixels, int width, int height, int x1, int y1, int x2, int y2, size_t color, bool blending) {
    bool x_l = x1 < x2;
    bool y_l = y1 < y2;

    int dx = x_l ? x2 - x1 : x1 - x2;
    int dy = y_l ? y2 - y1 : y1 - y2;
    int sx = x_l ? 1 : -1;
    int sy = y_l ? 1 : -1;

    int err = dx - dy;
    while (true) {
        setPixel(_pixels, width, height, x1, y1, color, blending);
        if (x1 == x2 && y1 == y2) {
            break;
        }
        int e2 = 2 * err;
        if (e2 > -dy) {
            err -= dy;
            x1 += sx;
        }
        if (e2 < dx) {
            err += dx;
            y1 += sy;
        }
    }
}

inline void _drawLineThick(size_t _pixels, int width, int height, int x1, int y1, int x2, int y2, size_t color, bool blending, int thickness) {
    if (thickness == 1) {
        _drawLine(_pixels, width, height, x1, y1, x2, y2, color, blending);
        return;
    }
    int s, f;
    if (thickness % 2 == 0) {
        s = -thickness / 2;
        f = thickness / 2;
    } else {
        s = -(thickness - 1) / 2;
        f = ((thickness - 1) / 2) + 1;
    }
    for (int x = s; x < f; x++) {
        for (int y = s; y < f; y++) {
            _drawLine(_pixels, width, height, x1 + x, y1 + y, x2 + x, y2 + y, color, blending);
        }
    }
}

inline void _aaDrawLine(size_t _pixels, int width, int height, int x1, int y1, int x2, int y2, size_t color, bool blending) {
    auto fpart = [](double x) { return (double) (x - floor(x)); };
    auto rfpart = [fpart](double x) { return 1 - fpart(x); };

    uint32_t color_u = (uint32_t) color;
    uint32_t colorRGB = color_u & CMASK;
    uint8_t colorA = (color_u & AMASK) >> 24;

    bool steep = abs(y2 - y1) > abs(x2 - x1);
    if (steep) {
        int temp = x1;
        x1 = y1;
        y1 = temp;
        temp = x2;
        x2 = y2;
        y2 = temp;
    }
    if (x1 > x2) {
        int temp = x1;
        x1 = x2;
        x2 = temp;
        temp = y1;
        y1 = y2;
        y2 = temp;
    }

    int dx = x2 - x1;
    int dy = y2 - y1;

    double gradient = 1;
    if (dx != 0) {
        gradient = (double) dy / (double) dx;
    }

    double intery = y1 + gradient;

    if (steep) {
        setPixel(_pixels, width, height, y1, x1, color, blending);
        setPixel(_pixels, width, height, y2, x2, color, blending);

        for (int x = x1 + 1; x < x2; x++) {
            setPixel(_pixels, width, height, (int) floor(intery), x, colorRGB | ((uint8_t) (rfpart(intery) * colorA)) << 24, blending);
            setPixel(_pixels, width, height, (int) floor(intery) + 1, x, colorRGB | ((uint8_t) (fpart(intery) * colorA)) << 24, blending);
            intery += gradient;
        }
    } else {
        setPixel(_pixels, width, height, x1, y1, color, blending);
        setPixel(_pixels, width, height, x2, y2, color, blending);

        for (int x = x1 + 1; x < x2; x++) {
            setPixel(_pixels, width, height, x, (int) floor(intery), colorRGB | ((uint8_t) (rfpart(intery) * colorA)) << 24, blending);
            setPixel(_pixels, width, height, x, (int) floor(intery) + 1, colorRGB | ((uint8_t) (fpart(intery) * colorA)) << 24, blending);
            intery += gradient;
        }
    }
}

inline void _aaDrawLineThick(size_t _pixels, int width, int height, int x1, int y1, int x2, int y2, size_t color, bool blending, int thickness) {
    if (thickness == 1) {
        _aaDrawLine(_pixels, width, height, x1, y1, x2, y2, color, blending);
        return;
    }
    int s, f;
    if (thickness % 2 == 0) {
        s = -thickness / 2;
        f = thickness / 2;
    } else {
        s = -(thickness - 1) / 2;
        f = ((thickness - 1) / 2) + 1;
    }
    for (int x = s; x < f; x++) {
        for (int y = s; y < f; y++) {
            if (x == s || y == s || x == f - 1 || y == f - 1) {
                _aaDrawLine(_pixels, width, height, x1 + x, y1 + y, x2 + x, y2 + y, color, blending);
            } else {
                _drawLine(_pixels, width, height, x1 + x, y1 + y, x2 + x, y2 + y, color, blending);
            }
        }
    }
}

inline void drawLine(size_t _pixels, int width, int height, int x1, int y1, int x2, int y2, size_t color, bool aa, bool blending, int thickness) {
    if (aa) _aaDrawLineThick(_pixels, width, height, x1, y1, x2, y2, color, blending, thickness);
    else _drawLineThick(_pixels, width, height, x1, y1, x2, y2, color, blending, thickness);
}

/***********************************************************************************************************************

CIRCLE FUNCTIONS

***********************************************************************************************************************/

inline void _drawCircle(size_t _pixels, int width, int height, int xc, int yc, int radius, size_t color, bool blending) {
    int x = radius;
    int y = 0;
    int E = -x;
    while (x >= y) {
        setPixel(_pixels, width, height, xc + x, yc + y, color, blending);
        setPixel(_pixels, width, height, xc - x, yc - y, color, blending);
        setPixel(_pixels, width, height, xc + y, yc + x, color, blending);
        setPixel(_pixels, width, height, xc - y, yc + x, color, blending);
        setPixel(_pixels, width, height, xc + x, yc - y, color, blending);
        setPixel(_pixels, width, height, xc - x, yc + y, color, blending);
        setPixel(_pixels, width, height, xc + y, yc - x, color, blending);
        setPixel(_pixels, width, height, xc - y, yc - x, color, blending);

        E += 2 * (y++) + 1;
        if (E >= 0) {
            E -= 2 * (x--) + 1;
        }
    }
}

inline void _drawCircleThick(size_t _pixels, int width, int height, int xc, int yc, int radius, size_t color, bool blending, int thickness) {
    if (thickness == 1) {
        _drawCircle(_pixels, width, height, xc, yc, radius, color, blending);
        return;
    }
    int inner, outer;
    if (thickness % 2 == 0) {
        outer = radius + (thickness / 2) - 1;
        inner = radius - (thickness / 2);
    } else {
        outer = radius + (thickness / 2);
        inner = radius - (thickness / 2);
    }
    int xo = outer;
    int xi = inner;
    int y = 0;
    int erro = 1 - xo;
    int erri = 1 - xi;

    while (xo >= y) {
        _drawLine(_pixels, width, height, xc + xi, yc + y, xc + xo, yc + y, color, blending);
        _drawLine(_pixels, width, height, xc + y, yc + xi, xc + y, yc + xo, color, blending);
        _drawLine(_pixels, width, height, xc - xo, yc + y, xc - xi, yc + y, color, blending);
        _drawLine(_pixels, width, height, xc - y, yc + xi, xc - y, yc + xo, color, blending);
        _drawLine(_pixels, width, height, xc - xo, yc - y, xc - xi, yc - y, color, blending);
        _drawLine(_pixels, width, height, xc - y, yc - xo, xc - y, yc - xi, color, blending);
        _drawLine(_pixels, width, height, xc + xi, yc - y, xc + xo, yc - y, color, blending);
        _drawLine(_pixels, width, height, xc + y, yc - xo, xc + y, yc - xi, color, blending);

        y++;

        if (erro < 0) {
            erro += 2 * y + 1;
        } else {
            xo--;
            erro += 2 * (y - xo + 1);
        }

        if (y > inner) {
            xi = y;
        } else {
            if (erri < 0) {
                erri += 2 * y + 1;
            } else {
                xi--;
                erri += 2 * (y - xi + 1);
            }
        }
    }
}

inline void _aaDrawCircle(size_t pixels, int width, int _height, int xc, int yc, int outer_radius, size_t color, bool blending) {
    auto _draw_point = [pixels, width, _height, xc, yc, color, blending](int x, int y, uint8_t alpha) {
        size_t c = (color & CMASK) | alpha << 24;
        setPixel(pixels, width, _height, xc + x, yc + y, c, blending);
        setPixel(pixels, width, _height, xc + x, yc - y, c, blending);
        setPixel(pixels, width, _height, xc - x, yc + y, c, blending);
        setPixel(pixels, width, _height, xc - x, yc - y, c, blending);
        setPixel(pixels, width, _height, xc - y, yc - x, c, blending);
        setPixel(pixels, width, _height, xc - y, yc + x, c, blending);
        setPixel(pixels, width, _height, xc + y, yc - x, c, blending);
        setPixel(pixels, width, _height, xc + y, yc + x, c, blending);
    };
    auto max = [](int a, int b) {
        return a > b ? a : b;
    };

    int i = 0;
    int j = outer_radius;
    double height;

    int sq_r = outer_radius * outer_radius;

    uint8_t last_fade_amount = 0;
    uint8_t fade_amount = 0;

    uint8_t MAX_OPAQUE = (color & AMASK) >> 24;

    while (i < j) {
        height = sqrt(max(sq_r - i * i, 0));
        fade_amount = MAX_OPAQUE * (ceil(height) - height);

        if (fade_amount < last_fade_amount) {
            j -= 1;
        }
        last_fade_amount = fade_amount;

        _draw_point(i, j, MAX_OPAQUE - fade_amount);
        _draw_point(i, j - 1, fade_amount);

        i += 1;
    }
}

inline void _aaDrawCircleThick(size_t _pixels, int width, int height, int xc, int yc, int outer_radius, size_t color, bool blending, int thickness) {
    if (thickness == 1) {
        _aaDrawCircle(_pixels, width, height, xc, yc, outer_radius, color, blending);
        return;
    }
    int inner, outer;
    if (thickness % 2 == 0) {
        outer = outer_radius + (thickness / 2) - 1;
        inner = outer_radius - (thickness / 2);
    } else {
        outer = outer_radius + (thickness / 2);
        inner = outer_radius - (thickness / 2);
    }
    _drawCircleThick(_pixels, width, height, xc, yc, outer_radius, color, blending, thickness);
    _aaDrawCircle(_pixels, width, height, xc, yc, inner, color, blending);
    _aaDrawCircle(_pixels, width, height, xc, yc, outer, color, blending);
}

inline void _fillCircle(size_t _pixels, int width, int height, int xc, int yc, int radius, size_t color, bool blending) {
    int x = radius;
    int y = 0;
    int E = -x;
    while (x >= y) {
        _drawLine(_pixels, width, height, xc + x, yc + y, xc - x, yc + y, color, blending);
        _drawLine(_pixels, width, height, xc - y, yc + x, xc + y, yc + x, color, blending);
        _drawLine(_pixels, width, height, xc - x, yc - y, xc + x, yc - y, color, blending);
        _drawLine(_pixels, width, height, xc - y, yc - x, xc + y, yc - x, color, blending);

        E += 2 * (y++) + 1;
        if (E >= 0) {
            E -= 2 * (x--) + 1;
        }
    }
}

inline void drawCircle(size_t _pixels, int width, int height, int xc, int yc, int radius, size_t borderColor, size_t fillColor, bool aa, bool blending, int thickness) {
    size_t color = borderColor;
    bool blend = blending;

    if (fillColor != 0) {
        _fillCircle(_pixels, width, height, xc, yc, radius, fillColor, blending);

        color = borderColor == 0 ? fillColor : borderColor;
        blend = true;
    }

    if (color != 0) {
        if (aa) {
            _aaDrawCircleThick(_pixels, width, height, xc, yc, radius, color, blend, thickness);
        } else {
            _drawCircleThick(_pixels, width, height, xc, yc, radius, color, blending, thickness);
        }
    }
}

/***********************************************************************************************************************

POLYGON FUNCTIONS

***********************************************************************************************************************/

inline void _drawPoly(size_t _pixels, int width, int height, void* vx, void* vy, int len, size_t color, bool blending, int thickness) {
    int* v_x = (int*) vx;
    int* v_y = (int*) vy;
    for (int i = 0; i < len; i++) {
        _drawLineThick(_pixels, width, height, v_x[i], v_y[i], v_x[(i + 1) % len], v_y[(i + 1) % len], color, blending, thickness);
    }
}

inline void _aaDrawPoly(size_t _pixels, int width, int height, void* vx, void* vy, int len, size_t color, bool blending, int thickness) {
    int* v_x = (int*) vx;
    int* v_y = (int*) vy;

    for (int i = 0; i < len; i++) {
        _aaDrawLineThick(_pixels, width, height, v_x[i], v_y[i], v_x[(i + 1) % len], v_y[(i + 1) % len], color, blending, thickness);
    }
}

inline void _fillPolyConvex(size_t _pixels, int width, int height, void* vx, void* vy, int len, size_t color, bool blending) {
    int* v_x_min = (int*) malloc(height * sizeof(int));
    int* v_x_max = (int*) malloc(height * sizeof(int));
    int* v_x = (int*) vx;
    int* v_y = (int*) vy;

    for (int i = 0; i < height; i++) {
        v_x_min[i] = width + 1;
        v_x_max[i] = -1;
    }

    for (int i = 0; i < len; i++) {
        int x1 = v_x[i], y1 = v_y[i], x2 = v_x[(i + 1) % len], y2 = v_y[(i + 1) % len];
        bool x_l = x1 < x2;
        bool y_l = y1 < y2;

        int dx = x_l ? x2 - x1 : x1 - x2;
        int dy = y_l ? y2 - y1 : y1 - y2;
        int sx = x_l ? 1 : -1;
        int sy = y_l ? 1 : -1;

        int err = dx - dy;
        while (true) {
            if (0 <= y1 && y1 < height) {
                if (x1 < v_x_min[y1])
                    v_x_min[y1] = x1;
                if (x1 > v_x_max[y1])
                    v_x_max[y1] = x1;
            }

            if (x1 == x2 && y1 == y2)
                break;

            int e2 = 2 * err;
            if (e2 > -dy) {
                err -= dy;
                x1 += sx;
            }
            if (e2 < dx) {
                err += dx;
                y1 += sy;
            }
        }
    }

    for (int i = 0; i < height; i++) {
        if (v_x_max[i] == -1) {
            continue;
        }
        _drawLine(_pixels, width, height, v_x_min[i], i, v_x_max[i], i, color, blending);
    }

    free(v_x_min);
    free(v_x_max);
}

inline void drawPoly(size_t _pixels, int width, int height, void* vx, void* vy, int len, size_t borderColor, size_t fillColor, bool aa, bool blending, int thickness) {
    size_t color = borderColor;
    bool blend = blending;

    if (fillColor != 0) {
        _fillPolyConvex(_pixels, width, height, vx, vy, len, fillColor, blending);

        color = borderColor == 0 ? fillColor : borderColor;
        blend = true;
    }

    if (color != 0) {
        if (aa) {
            _aaDrawPoly(_pixels, width, height, vx, vy, len, color, blend, thickness);
        } else {
            _drawPoly(_pixels, width, height, vx, vy, len, color, blending, thickness);
        }
    }
}

/***********************************************************************************************************************

RECTANGLE FUNCTIONS

***********************************************************************************************************************/

inline void _drawRect(size_t _pixels, int width, int height, int x, int y, int w, int h, size_t color, bool blending) {
    for (int i = x; i < w + x; i++) {
        setPixel(_pixels, width, height, i, y, color, blending);
        setPixel(_pixels, width, height, i, y + h - 1, color, blending);
    }
    for (int i = y; i < h + y; i++) {
        setPixel(_pixels, width, height, x, i, color, blending);
        setPixel(_pixels, width, height, x + w - 1, i, color, blending);
    }
}

inline void _drawRectThick(size_t _pixels, int width, int height, int x, int y, int w, int h, size_t color, bool blending, int thickness) {
    if (thickness == 1) {
        _drawRect(_pixels, width, height, x, y, w, h, color, blending);
    } else {
        for (int i = -thickness / 2; i <= thickness / 2; i++) {
            _drawRect(_pixels, width, height, x + i, y + i, w - (2 * i), h - (2 * i), color, blending);
        }
    }
}

inline void _fillRect(size_t _pixels, int width, int height, int x, int y, int w, int h, size_t color, bool blending) {
    for (int i = y; i < h + y; i++) {
        for (int j = x; j < w + x; j++) {
            setPixel(_pixels, width, height, j, i, color, blending);
        }
    }
}

inline void drawRect(size_t _pixels, int width, int height, int x, int y, int w, int h, size_t borderColor, size_t fillColor, bool blending, int thickness) {
    if (fillColor != 0) {
        _fillRect(_pixels, width, height, x, y, w, h, fillColor, blending);
    }
    if (borderColor != 0) {
        _drawRectThick(_pixels, width, height, x, y, w, h, borderColor, blending, thickness);
    }
}
