# HTML5 Tags & CSS3 Properties — Quick Reference

---

## HTML5 Tags

---

### 1. `<section>`

**What it does:** Groups related content into a thematic section of a page.

**Attributes:**
| Attribute | Description | Example |
| :--- | :--- | :--- |
| `id` | Unique identifier for linking/styling | `id="about"` |
| `class` | CSS class name | `class="hero-section"` |
| `aria-label` | Accessibility label for screen readers | `aria-label="About Us"` |

**Where to use:** Page regions like Hero, About, Services, Contact sections.

```html
<section id="about" class="hero-section" aria-label="About Us">
  <h2>About Us</h2>
  <p>We build modern web apps.</p>
</section>
```

---

### 2. `<article>`

**What it does:** Represents self-contained, independently distributable content.

**Attributes:**
| Attribute | Description | Example |
| :--- | :--- | :--- |
| `id` | Unique ID | `id="post-1"` |
| `class` | CSS class | `class="blog-post"` |
| `lang` | Language of the article content | `lang="en"` |

**Where to use:** Blog posts, news articles, forum entries, product cards.

```html
<article id="post-1" class="blog-post">
  <h3>My First Post</h3>
  <p>Published on Oct 2026</p>
</article>
```

---

### 3. `<nav>`

**What it does:** Defines a block of navigation links.

**Attributes:**
| Attribute | Description | Example |
| :--- | :--- | :--- |
| `id` | Unique identifier | `id="main-nav"` |
| `class` | CSS class | `class="navbar"` |
| `aria-label` | Describes the navigation purpose | `aria-label="Main Navigation"` |

**Where to use:** Top navigation bars, sidebar menus, breadcrumb links, footer nav.

```html
<nav id="main-nav" aria-label="Main Navigation">
  <a href="#home">Home</a>
  <a href="#about">About</a>
  <a href="#contact">Contact</a>
</nav>
```

---

### 4. `<header>`

**What it does:** Defines the introductory content or navigational aids for a page or section.

**Attributes:**
| Attribute | Description | Example |
| :--- | :--- | :--- |
| `id` | Unique ID | `id="site-header"` |
| `class` | CSS class | `class="top-bar"` |
| `role` | ARIA role for accessibility | `role="banner"` |

**Where to use:** Top of page (site header), top of `<article>` or `<section>`.

```html
<header id="site-header" role="banner">
  <h1>My Website</h1>
  <nav>...</nav>
</header>
```

---

### 5. `<footer>`

**What it does:** Defines the footer for a page or section — typically contains copyright, links, contact info.

**Attributes:**
| Attribute | Description | Example |
| :--- | :--- | :--- |
| `id` | Unique ID | `id="site-footer"` |
| `class` | CSS class | `class="footer"` |
| `role` | ARIA role | `role="contentinfo"` |

**Where to use:** Bottom of the page, bottom of articles or sections.

```html
<footer id="site-footer" role="contentinfo">
  <p>&copy; 2026 My Website. All rights reserved.</p>
</footer>
```

---

### 6. `<figure>` and `<figcaption>`

**What it does:** Wraps self-contained media (image, chart, code) with an optional caption.

**Attributes for `<figure>`:**
| Attribute | Description | Example |
| :--- | :--- | :--- |
| `id` | Unique ID | `id="fig-1"` |
| `class` | CSS class | `class="image-block"` |

**Attributes for `<figcaption>`:**
| Attribute | Description | Example |
| :--- | :--- | :--- |
| `class` | CSS class | `class="caption"` |

**Where to use:** Images with captions, charts, code snippets, diagrams in articles.

```html
<figure id="fig-1" class="image-block">
  <img src="chart.png" alt="Sales Chart">
  <figcaption class="caption">Fig 1: Monthly Sales Data</figcaption>
</figure>
```

---

### 7. `<input>` (HTML5 types)

**What it does:** Creates interactive form controls for user input.

**Key Attributes:**
| Attribute | Description | Example |
| :--- | :--- | :--- |
| `type` | Input type (text, email, number, date, range, color, search, tel, url, password) | `type="email"` |
| `id` | Links the input to a `<label>` | `id="email"` |
| `name` | Form field name sent to server | `name="email"` |
| `placeholder` | Hint text shown inside input | `placeholder="Enter email"` |
| `required` | Makes field mandatory | `required` |
| `min` / `max` | Range limits for number/date | `min="1" max="100"` |
| `pattern` | Regex validation pattern | `pattern="[A-Za-z]+"` |
| `autocomplete` | Enable/disable browser autocomplete | `autocomplete="off"` |
| `disabled` | Disables the input | `disabled` |
| `readonly` | Makes input read-only | `readonly` |

**Where to use:** Registration forms, login forms, search bars, settings pages.

```html
<label for="email">Email:</label>
<input type="email" id="email" name="email"
       placeholder="you@example.com" required autocomplete="off">

<label for="age">Age:</label>
<input type="number" id="age" name="age" min="1" max="120">

<label for="dob">Date of Birth:</label>
<input type="date" id="dob" name="dob">
```

---

### 8. `<video>`

**What it does:** Embeds a video player directly in the page.

**Attributes:**
| Attribute | Description | Example |
| :--- | :--- | :--- |
| `src` | Path or URL to video file | `src="demo.mp4"` |
| `controls` | Shows play/pause/volume controls | `controls` |
| `autoplay` | Starts playing automatically | `autoplay` |
| `muted` | Mutes audio (required for autoplay in browsers) | `muted` |
| `loop` | Loops the video | `loop` |
| `poster` | Image shown before video loads | `poster="thumb.jpg"` |
| `width` / `height` | Dimensions | `width="640" height="360"` |
| `preload` | Hints to browser (auto / metadata / none) | `preload="metadata"` |

**Where to use:** Hero background videos, tutorial embeds, product demos.

```html
<video src="intro.mp4" controls poster="thumb.jpg"
       width="640" height="360" preload="metadata">
  Your browser does not support the video tag.
</video>
```

---

### 9. `<details>` and `<summary>`

**What it does:** Creates a native expandable/collapsible disclosure widget without JavaScript.

**Attributes for `<details>`:**
| Attribute | Description | Example |
| :--- | :--- | :--- |
| `open` | Starts in expanded state | `open` |
| `id` | Unique ID | `id="faq-1"` |
| `class` | CSS class | `class="faq-item"` |

**Where to use:** FAQ sections, collapsible settings, spoiler/hint boxes, documentation.

```html
<details id="faq-1" class="faq-item">
  <summary>What is MongoDB?</summary>
  <p>MongoDB is a NoSQL document database that stores data in JSON-like format.</p>
</details>

<details open>
  <summary>Already expanded by default</summary>
  <p>This content is visible immediately.</p>
</details>
```

---

### 10. `<canvas>`

**What it does:** Provides a drawing surface for 2D graphics using JavaScript.

**Attributes:**
| Attribute | Description | Example |
| :--- | :--- | :--- |
| `id` | Used by JavaScript to get reference | `id="myCanvas"` |
| `width` | Canvas width in pixels | `width="800"` |
| `height` | Canvas height in pixels | `height="400"` |
| `class` | CSS class | `class="game-canvas"` |

**Where to use:** Charts, data visualisations, games, animations, image manipulation.

```html
<canvas id="myCanvas" width="800" height="400" class="game-canvas">
  Your browser does not support the canvas element.
</canvas>

<script>
  const canvas = document.getElementById("myCanvas");
  const ctx = canvas.getContext("2d");
  ctx.fillStyle = "#3b82f6";
  ctx.fillRect(50, 50, 200, 100);
</script>
```

---

### 11. `<datalist>`

**What it does:** Provides a list of predefined autocomplete suggestions for an `<input>`.

**Attributes:**
| Attribute | Description | Example |
| :--- | :--- | :--- |
| `id` | Must match the `list` attribute of the linked `<input>` | `id="departments"` |

**Where to use:** Search bars, form fields with common suggestions (cities, departments, tags).

```html
<label for="dept">Department:</label>
<input type="text" id="dept" list="departments" placeholder="Type a department">
<datalist id="departments">
  <option value="Computer Science">
  <option value="Information Technology">
  <option value="Electronics">
  <option value="Mechanical">
</datalist>
```

---

### 12. `<progress>`

**What it does:** Displays a progress bar showing completion of a task.

**Attributes:**
| Attribute | Description | Example |
| :--- | :--- | :--- |
| `value` | Current progress value | `value="70"` |
| `max` | Maximum value (default 1.0) | `max="100"` |
| `id` | Unique ID | `id="upload-progress"` |
| `class` | CSS class | `class="progress-bar"` |

**Where to use:** File uploads, form completion indicators, quiz progress, loading states.

```html
<label for="upload-progress">Upload Progress:</label>
<progress id="upload-progress" value="70" max="100" class="progress-bar">
  70%
</progress>
```

---

&nbsp;

---

## CSS3 Properties

---

### 1. `border-radius`

**What it does:** Rounds the corners of an element's border box.

**Syntax:** `border-radius: <value>`

| Value | Result |
| :--- | :--- |
| `8px` | Slightly rounded corners |
| `50%` | Makes element a circle (if width = height) |
| `10px 0` | Rounds top-left + bottom-right only |
| `top-left top-right bottom-right bottom-left` | Individual corner control |

**Where to use:** Buttons, cards, profile pictures, badges, input fields.

```css
.btn {
  border-radius: 8px;
}

.avatar {
  border-radius: 50%;   /* circle */
}

.card {
  border-radius: 12px 12px 0 0;  /* rounded only at top */
}
```

---

### 2. `box-shadow`

**What it does:** Adds one or more shadow effects around an element.

**Syntax:** `box-shadow: offset-x offset-y blur-radius spread-radius color`

| Value | Description |
| :--- | :--- |
| `2px 4px 8px rgba(0,0,0,0.2)` | Soft drop shadow |
| `0 0 10px blue` | Glow effect |
| `inset 0 2px 4px rgba(0,0,0,0.3)` | Inner (pressed) shadow |

**Where to use:** Cards, modals, buttons (hover), image borders.

```css
.card {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.btn:hover {
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.5);
}
```

---

### 3. `transition`

**What it does:** Smoothly animates a property change over a given duration.

**Syntax:** `transition: property duration timing-function delay`

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `property` | Which CSS property to animate | `background-color`, `all` |
| `duration` | How long the animation lasts | `0.3s` |
| `timing-function` | Speed curve | `ease`, `linear`, `ease-in-out` |
| `delay` | Wait before starting | `0.1s` |

**Where to use:** Button hover effects, menu show/hide, colour fades, card lifts.

```css
.btn {
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.btn:hover {
  background-color: #2563eb;
  transform: translateY(-2px);
}
```

---

### 4. `transform`

**What it does:** Applies 2D/3D geometric transformations to an element.

**Common Functions:**
| Function | Description | Example |
| :--- | :--- | :--- |
| `translate(x, y)` | Moves element | `translate(10px, 20px)` |
| `scale(x, y)` | Resizes element | `scale(1.1)` |
| `rotate(deg)` | Rotates element | `rotate(45deg)` |
| `skew(x, y)` | Skews element | `skew(10deg)` |

**Where to use:** Hover animations, loading spinners, card flips, icon animations.

```css
.card:hover {
  transform: scale(1.05) translateY(-4px);
}

.icon {
  transform: rotate(180deg);
  transition: transform 0.3s ease;
}
```

---

### 5. `flexbox` (`display: flex`)

**What it does:** Makes a container use the Flexible Box Layout model for aligning and distributing children.

**Key Properties:**
| Property | Description | Values |
| :--- | :--- | :--- |
| `flex-direction` | Row or column layout | `row`, `column`, `row-reverse` |
| `justify-content` | Align items on main axis | `center`, `space-between`, `flex-end` |
| `align-items` | Align items on cross axis | `center`, `stretch`, `flex-start` |
| `flex-wrap` | Allow wrapping | `wrap`, `nowrap` |
| `gap` | Space between items | `16px`, `1rem` |

**Where to use:** Navbars, card grids, centering elements, form layouts.

```css
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
}

.card-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
}
```

---

### 6. `grid` (`display: grid`)

**What it does:** Creates a two-dimensional layout system with rows and columns.

**Key Properties:**
| Property | Description | Example |
| :--- | :--- | :--- |
| `grid-template-columns` | Defines column sizes | `repeat(3, 1fr)` |
| `grid-template-rows` | Defines row sizes | `auto 1fr auto` |
| `gap` / `column-gap` / `row-gap` | Spacing between cells | `gap: 20px` |
| `grid-column` | Span a cell across columns | `grid-column: 1 / 3` |
| `grid-row` | Span a cell across rows | `grid-row: 1 / 3` |

**Where to use:** Page layouts, dashboards, photo galleries, responsive card grids.

```css
.layout {
  display: grid;
  grid-template-columns: 250px 1fr;
  grid-template-rows: auto 1fr auto;
  gap: 20px;
  min-height: 100vh;
}

.gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
```

---

### 7. `@keyframes` and `animation`

**What it does:** Defines and applies custom animations.

**`animation` shorthand:** `animation: name duration timing-function delay iteration-count direction`

| Property | Description | Example |
| :--- | :--- | :--- |
| `animation-name` | Name of `@keyframes` block | `fadeIn` |
| `animation-duration` | How long one cycle takes | `1s` |
| `animation-timing-function` | Speed curve | `ease-in-out` |
| `animation-iteration-count` | How many times to repeat | `infinite`, `3` |
| `animation-direction` | Forward, reverse or alternate | `alternate` |
| `animation-fill-mode` | State after animation ends | `forwards` |

**Where to use:** Loading spinners, page entry effects, pulsing icons, skeleton loaders.

```css
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

.hero-text {
  animation: fadeIn 0.6s ease-out forwards;
}

.spinner {
  animation: spin 1s linear infinite;
}
```

---

### 8. `linear-gradient` and `radial-gradient`

**What it does:** Creates smooth colour transitions as a background image.

**Syntax:**
- `linear-gradient(direction, color1, color2, ...)`
- `radial-gradient(shape, color1, color2, ...)`

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `direction` | Angle or keyword | `to right`, `135deg` |
| `color stops` | Colour + optional position | `#3b82f6 0%, #9333ea 100%` |

**Where to use:** Hero section backgrounds, button fills, progress bars, card overlays.

```css
.hero {
  background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
}

.btn {
  background: linear-gradient(to right, #6366f1, #8b5cf6);
}

.radial-bg {
  background: radial-gradient(circle at center, #fff 0%, #e0e7ff 100%);
}
```

---

### 9. `backdrop-filter`

**What it does:** Applies visual effects (blur, brightness, etc.) to the area *behind* an element — used for glassmorphism.

**Common Values:**
| Value | Effect |
| :--- | :--- |
| `blur(10px)` | Blurs content behind element |
| `brightness(0.8)` | Darkens content behind |
| `saturate(1.5)` | Boosts colour saturation behind |

**Where to use:** Glassmorphism cards, frosted-glass navbars, modal overlays, sidebars.

```css
.glass-card {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);   /* Safari */
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
}
```

---

### 10. `var()` (CSS Custom Properties / Variables)

**What it does:** Defines reusable values (tokens) that can be used throughout the stylesheet.

**Syntax:**
- Declare: `--variable-name: value;`
- Use: `property: var(--variable-name, fallback);`

**Where to use:** Design systems, theming (light/dark mode), maintaining consistent colours, spacing, and font sizes.

```css
/* Declare in :root for global access */
:root {
  --color-primary: #3b82f6;
  --color-danger:  #dc2626;
  --font-size-lg:  1.125rem;
  --border-radius: 8px;
  --shadow:        0 4px 16px rgba(0, 0, 0, 0.15);
}

.btn {
  background-color: var(--color-primary);
  border-radius: var(--border-radius);
  font-size: var(--font-size-lg);
  box-shadow: var(--shadow);
}

.btn-danger {
  background-color: var(--color-danger);
}
```

---

### 11. `media queries` (`@media`)

**What it does:** Applies CSS rules only when certain conditions (screen size, orientation) are met — used for responsive design.

**Syntax:** `@media (condition) { ... }`

| Breakpoint | Typical Use | Example |
| :--- | :--- | :--- |
| `max-width: 768px` | Mobile | `@media (max-width: 768px)` |
| `min-width: 769px` | Tablet and above | `@media (min-width: 769px)` |
| `min-width: 1024px` | Desktop | `@media (min-width: 1024px)` |
| `prefers-color-scheme: dark` | Dark mode | `@media (prefers-color-scheme: dark)` |

**Where to use:** Making layouts responsive — stacking columns on mobile, hiding sidebar on small screens.

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

/* On tablets — 2 columns */
@media (max-width: 1024px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* On mobile — 1 column */
@media (max-width: 600px) {
  .card-grid {
    grid-template-columns: 1fr;
  }
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  body {
    background: #0f172a;
    color: #f1f5f9;
  }
}
```

---

### 12. `clip-path`

**What it does:** Clips (crops) an element to a defined shape.

**Common Values:**
| Value | Shape |
| :--- | :--- |
| `circle(50%)` | Circle |
| `ellipse(50% 30%)` | Ellipse |
| `polygon(0 0, 100% 0, 80% 100%, 0 100%)` | Custom polygon |
| `inset(10px)` | Rectangle with inset |

**Where to use:** Hero section diagonal cuts, image shape cropping, creative card designs, ribbon effects.

```css
.hero {
  clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);
}

.avatar {
  clip-path: circle(50%);
}

.diagonal-divider {
  clip-path: polygon(0 0, 100% 0, 100% 80%, 0 100%);
}
```
