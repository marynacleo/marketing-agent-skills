<?php
/**
 * Plugin Name: FAQ Hub
 * Description: Per-page FAQs via [faq] that auto-aggregate into a central hub via [faq_hub].
 *   Pages declare FAQs inline; the hub scans all published pages and groups them (with links back
 *   = internal interlinking). Outputs FAQPage JSON-LD for SEO/AI answers. kses-safe (this PHP),
 *   no post_content rewriting. Accordions use native <details>, styled with the site's design tokens.
 *
 * Usage on any page:   [faq q="When is the balance due?"]The balance is due 8 weeks before departure.[/faq]
 * Usage on /faq/ hub:  [faq_hub]
 */
if (!defined('ABSPATH')) exit;

global $faq_collected;
$faq_collected = [];

/* ---------- per-page FAQ item ---------- */
add_shortcode('faq', function ($atts, $content = '') {
    global $faq_collected;
    $atts = shortcode_atts(['q' => ''], $atts, 'faq');
    $q = trim($atts['q']);
    $a = trim(do_shortcode($content));
    if ($q === '') return '';
    $faq_collected[] = ['q' => $q, 'a' => $a];
    return '<details class="faq"><summary>' . esc_html($q) . '</summary><div class="faq-a">' . wpautop($a) . '</div></details>';
});

/* ---------- collect FAQs across all published pages ---------- */
function faq_collect_all() {
    $cached = get_transient('faq_index');
    if ($cached !== false) return $cached;

    $out = [];
    $pages = get_posts(['post_type' => ['page', 'post'], 'post_status' => 'publish', 'numberposts' => -1]);
    $hub_id = get_queried_object_id();
    foreach ($pages as $p) {
        if (strpos($p->post_content, '[faq ') === false) continue;
        if (preg_match_all('/\[faq\s+q="([^"]*)"\]([\s\S]*?)\[\/faq\]/', $p->post_content, $m, PREG_SET_ORDER)) {
            $items = [];
            foreach ($m as $one) {
                $items[] = ['q' => trim($one[1]), 'a' => trim(wp_strip_all_tags(do_shortcode($one[2]), false))];
            }
            if ($items) {
                $title = preg_replace('/\s*[\x{2014}\x{2013}]\s*/u', ' - ', get_the_title($p)); // no em/en dashes
                $out[] = ['title' => $title, 'url' => get_permalink($p), 'id' => $p->ID, 'items' => $items];
            }
        }
    }
    set_transient('faq_index', $out, HOUR_IN_SECONDS);
    return $out;
}
// rebuild index when any page is saved
add_action('save_post', function () { delete_transient('faq_index'); });

/* ---------- the hub ---------- */
add_shortcode('faq_hub', function () {
    $groups = faq_collect_all();
    if (!$groups) return '<p>FAQs are coming soon.</p>';
    $html = '<div class="faq-hub">';
    foreach ($groups as $g) {
        $html .= '<section class="faq-group"><h2>' . esc_html($g['title']) . '</h2>';
        foreach ($g['items'] as $it) {
            $html .= '<details class="faq"><summary>' . esc_html($it['q']) . '</summary><div class="faq-a">' . wpautop($it['a']) . '</div></details>';
        }
        $html .= '<p class="faq-more"><a href="' . esc_url($g['url']) . '">More on ' . esc_html($g['title']) . ' &rarr;</a></p></section>';
    }
    $html .= '</div>';
    return $html;
});

/* ---------- FAQPage JSON-LD ---------- */
add_action('wp_footer', function () {
    global $faq_collected;
    $faqs = $faq_collected;
    // on the hub page, include everything
    if (is_page() && has_shortcode(get_post_field('post_content', get_queried_object_id()), 'faq_hub')) {
        foreach (faq_collect_all() as $g) foreach ($g['items'] as $it) $faqs[] = $it;
    }
    if (!$faqs) return;
    $main = [];
    $seen = [];
    foreach ($faqs as $f) {
        $q = trim($f['q']); if ($q === '' || isset($seen[$q])) continue; $seen[$q] = 1;
        $main[] = ['@type' => 'Question', 'name' => $q,
            'acceptedAnswer' => ['@type' => 'Answer', 'text' => trim(wp_strip_all_tags($f['a']))]];
    }
    if (!$main) return;
    $schema = ['@context' => 'https://schema.org', '@type' => 'FAQPage', 'mainEntity' => $main];
    echo "\n<script type=\"application/ld+json\">" . wp_json_encode($schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . "</script>\n";
}, 20);

/* ---------- styling (design tokens, native details accordion) ---------- */
add_action('wp_footer', function () {
    ?>
<style id="faq-css">
.faq{border:1px solid #E2E8F0;border-radius:12px;margin:0 0 12px;background:#fff;overflow:hidden}
.faq summary{cursor:pointer;list-style:none;padding:16px 48px 16px 18px;font-weight:600;color:#1A1A2E;position:relative;font-size:1rem;line-height:1.45}
.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:"+";position:absolute;right:18px;top:50%;transform:translateY(-50%);font-size:1.4rem;font-weight:400;color:#2B9FD9;transition:transform .2s}
.faq[open] summary:after{content:"\2212"}
.faq[open] summary{color:#1E7BB0}
.faq-a{padding:0 18px 16px;color:#374151;line-height:1.65}
.faq-a p{margin:0 0 10px}
.faq-a a{color:#1E7BB0;font-weight:600}
.faq-hub .faq-group{margin:0 0 30px;padding:18px 20px;background:#F7FBFE;border:1px solid #E2E8F0;border-radius:16px}
.faq-hub .faq-group h2{font-family:'Playfair Display',Georgia,serif;font-size:1.25rem;color:#1E7BB0;margin:0 0 14px;padding-left:12px;border-left:4px solid #F7941D}
.faq-more{margin:10px 0 0}
.faq-more a{color:#1E7BB0;font-weight:600;font-size:.9rem}
</style>
    <?php
}, 21);
