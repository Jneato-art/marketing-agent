---
name: short-form-video
description: Script and produce scroll-stopping short-form video for TikTok, Reels, and YouTube Shorts - hook-first scripting, retention structure - and generate it with the connected Higgsfield tools. Use when you need viral-style short video creative.
---

# Skill: Short-Form Video

Short-form video is the dominant organic and paid-social format. The first 3 seconds decide everything: over 80% of content is ignored within 3 seconds, and videos that retain 60%+ past the 3-second mark get pushed by the algorithm. This skill scripts hook-first videos and produces them with the connected Higgsfield tools.

## When to use
- You need TikTok/Reels/Shorts creative for organic growth or paid social.
- A brand's videos get views but no retention or conversion.
- You want a batch of hook variants to test.

## Connected tool (Higgsfield)
Use these tools - call them by name:
- `generate_video` - generate the video from the script/prompt.
- `show_marketing_studio` - open the marketing studio for ad-style short-form creative.
- `virality_predictor` - score a video for hook strength, retention risk, and predicted performance *before* you post; use it to pick the best cut.
- Supporting: `generate_image` / `generate_audio` for thumbnails, B-roll, voiceover; `media_upload_widget` when the user has a local clip to use as input.

Workflow: script -> `generate_video` (and `show_marketing_studio` for ad formats) -> `virality_predictor` to choose the winner -> post the highest-scoring cut.

## Hook-first scripting

Spoken hook lands in the first 3 seconds (~10-14 words). Rotate 5-10 hook formulas rather than reusing one. High-performing formulas:
- **Contrarian claim**: "Everything you've been told about X is wrong."
- **Mistake warning**: "Stop doing X if you want Y."
- **List tease**: "3 things I wish I knew before X."
- **Result/proof**: "How I got [result] in [timeframe]."
- **Curiosity gap**: "This is why X never works for you."

Script structure (works at 35-220 words; ~70-110 for a 30s video):
```
Hook (0-3s)  ->  Tension (why it matters)  ->  Value beats (2-4 quick points)
  ->  Proof/example  ->  Payoff  ->  CTA
```
Keep lines short and spoken. One clear payoff. Caption + on-screen text reinforce the hook for sound-off viewers.

## Procedure

1. **Set the goal & platform.** Awareness vs. conversion; TikTok vs. Reels vs. Shorts (aspect ratio, length, tone).
2. **Pick the angle** from `messaging.md` (a pillar or before/after).
3. **Write 3-5 hook variants** using different formulas above.
4. **Write the full script** in the structure above for the best 1-2 hooks.
5. **Generate** with Higgsfield `generate_video` (use `show_marketing_studio` for ad creative; `generate_audio`/`generate_image` for VO and B-roll).
6. **Predict & pick.** Run `virality_predictor` on each cut; post the highest-scoring one, hold the rest for re-testing.
7. **Post, then iterate** on the winning hook formula - rotate, don't repeat.
8. **Save** scripts + virality scores to `knowledge/brands/<brand>/short-form.md`.

## Output
- A batch of scripted videos (hook variants + full scripts), generated cuts, and virality scores, with a recommendation on which to post first.

## Self-learning
Log hook formula -> retention/views and virality score -> actual performance in `knowledge/experiments/experiments-log.md`. Promote the hook formulas that consistently win for this audience to `knowledge/index.md`.
