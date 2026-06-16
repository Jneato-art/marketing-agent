---
name: ad-creative-brief
description: Brief and generate ad creative (static and video) grounded in the brand and proven ad formats. Use when the plan needs ads, social creative, or visuals.
---

# Skill: Ad Creative Brief

## When to use
When a channel needs creative — paid ads, organic posts, landing visuals, video.

## Procedure

1. **Pull the brand.** Colors, logo, voice, product shots. If a Bloom brand exists, use it as the reference so output is on-brand.
2. **Pick the angle.** Tie to a researched audience pain/desire and the winning hook. One angle per concept.
3. **Choose a proven format.** Don't start from blank — recreate formats that already work (problem/solution, before/after, UGC testimonial, founder-to-camera, comparison).
4. **Write the brief** per concept: hook (first 3 seconds / headline), key message, visual direction, CTA, format/aspect ratio, channel.
5. **Generate.**
   - Static / ad images -> Bloom (`bloom_find_reference_ads` then `bloom_generate_image` with brand references).
   - Video / short-form -> Higgsfield (`generate_video`, `show_marketing_studio`); optionally check `virality_predictor`.
6. **Produce variations.** At least 3 concepts so there is something to test.

## Creative brief format

```
Concept #N — <angle>
Hook: <first line / 3 seconds>
Message: <one idea>
Visual: <direction>
Format: <e.g. 9:16 video, 1:1 image>
CTA: <action>
Channel: <where it runs>
```

## Output
3+ briefed concepts and the generated assets, linked in `knowledge/brands/<brand>/assets.md`.

## Self-learning
After the ads run, record winning hook + format in `playbooks-learned/` so the next creative round starts from a proven base.
