---
name: brand-asset-studio
description: Generate on-brand images and ad creative using the connected Bloom tools - pulling brand references and proven real-ad formats so output looks like the brand and converts. Use when you need static images, social creative, or ad visuals.
---

# Skill: Brand Asset Studio

Generic AI images look generic. Bloom is brand-aware: it pulls from the brand's own reference library and a curated library of real, high-performing ads, so output is on-brand and built on proven formats. This skill is the workflow for producing static images and ad creative.

## When to use
- You need on-brand images: social posts, ad creatives, hero images, product shots.
- You are building an ad and a proven format would beat a blank-prompt generation.

## Connected tool (Bloom) - canonical workflow
Use these tools - call them by name, in this order:
1. `bloom_list_brands` - find the brand to work in.
2. `bloom_search_user_images` (or `bloom_list_images`) - pull existing brand references; they measurably improve outputs.
3. For ads: `bloom_find_reference_ads` - surface real, high-performing ads in this category to recreate instead of generating from a blank prompt.
4. `bloom_generate_image` - generate, passing `reference_image_ids` (the brand refs and/or the chosen reference ad) so the output stays on-brand.
5. Refine: `bloom_edit_image`, `bloom_resize_image` (for placements/aspect ratios), `bloom_remove_background`, `bloom_upscale_image` as needed.
6. Collect: `bloom_list_images` with `wait: true` (or `bloom_get_image` with `wait: true`) - generation is async (~60-90s). Do not poll in a loop; `wait` is the intended path. Fire multiple `bloom_generate_image` calls in parallel when making a batch.

## Procedure

1. **Confirm brand & goal.** `bloom_list_brands`; clarify the asset (placement, platform, dimensions) and the message from `messaging.md`.
2. **Gather references.** `bloom_search_user_images` for brand look; for ads, `bloom_find_reference_ads` to find a proven format to adapt.
3. **Write the prompt.** Encode the offer/message, the visual style, and the desired emotion. Reference the message pillar the visual must carry.
4. **Generate on-brand.** `bloom_generate_image` with `reference_image_ids` set. Make 3-4 variants in parallel for testing.
5. **Resize for placements.** `bloom_resize_image` to each platform's spec (feed, story, square, etc.).
6. **Collect with `wait: true`**, review against brand and message, and pick variants to test.
7. **Hand winners to creative testing** (`growth-experiments`) and store specs in `knowledge/brands/<brand>/creative.md`.

## Tie-ins
- Pair with `ad-creative-brief` (the brief feeds the prompt) and `short-form-video` (Higgsfield) when you need motion instead of static.
- Static images -> Bloom. Video -> Higgsfield.

## Output
- A set of on-brand, placement-ready image/ad variants with the prompt and reference IDs recorded so winners are reproducible.

## Self-learning
Log which visual style, format, and reference ad won (CTR/engagement) in `knowledge/experiments/experiments-log.md`. Promote winning creative formats to `knowledge/index.md` so future generations start from what converts for this brand.
