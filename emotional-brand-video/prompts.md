# Feel-First AI-Video Prompt Library (portable, free-first)

Prompts are generator-agnostic: the same prompt works in Sora, Grok, Meta AI,
Kling, Hailuo, Veo (Gemini) and Pika, with small per-tool adjustments (cheat
sheet at the end). Write prompts in English even for FR brands; add on-screen
text later in editing, not in generation (generators render text badly).

Free-first rule: Sora ships with a ChatGPT Plus subscription, Grok and Meta AI
work without paid plans, and Kling / Hailuo / Veo / Pika all have free tiers
whose credits change, so verify before a session. No paid API key or plan is
needed for this method.

## 1. The base formula

Every Feel-First prompt is assembled from 8 slots, in this order:

```
[SUBJECT] [ACTION], [SETTING], [CAMERA + POV], [LIGHT], [MOOD], [SENSORY DETAIL], [TECH CUE]
```

1. **SUBJECT** - one real-looking person (or hands), specific: age feel, clothing, no model look.
2. **ACTION** - one simple everyday gesture, mid-action, natural pace.
3. **SETTING** - concrete place with regional character (plug in the brand's world).
4. **CAMERA + POV** - subjective/intimate framing + one believable move.
5. **LIGHT** - natural source, time of day.
6. **MOOD** - the ONE emotion of this scene.
7. **SENSORY DETAIL** - steam, dust in light, texture, fabric, skin, sound-implying detail.
8. **TECH CUE** - authenticity anchor: "shot on ARRI Alexa 35, 35mm lens, shallow depth of
   field, documentary style" (or Sony FX3). This cue reliably pushes generators toward
   realism.

### Base prompt skeleton (copy-paste)

```
Documentary style, hyperrealistic. [SUBJECT], [ACTION], in [SETTING].
[CAMERA]: [one move, slow and believable], point-of-view framing.
Natural light: [source, time of day]. Mood: [one emotion].
Fine textures: [2-3 sensory details]. Shot on ARRI Alexa 35, 35mm lens,
shallow depth of field. Real skin texture, natural color grading, slight
handheld movement. No text, no logos.
```

## 2. Standard negative prompt (append everywhere)

```
Negative: stock footage look, studio lighting, posed smiling models, oversaturated colors,
fast artificial camera movements, spinning transitions, motion graphics, text overlays,
watermark, logo, CGI look, plastic skin, extra fingers, distorted faces, warped hands,
morphing objects, jerky motion, fisheye distortion
```

Tools without a negative field (Sora, Grok, Meta): fold the critical ones into the prompt as
"avoid: stock-footage look, studio lighting, posed models, CGI look".

## 3. Per-scene templates (the 4-scene arc)

Generate each scene as a SEPARATE clip (5-10 s each, trim in edit). Keep SUBJECT, SETTING,
LIGHT and grading words identical across all four prompts of one video, so the scenes cut
together as one story. If the tool supports image-to-video, generate scene 2 first, screenshot
its last frame, and feed it as the start image of scene 3 for continuity.

### Scene 1 - Hook (2 s used)

Goal: one arresting sensory image, extreme close-up or unexpected POV.

```
Documentary style, hyperrealistic. Extreme close-up: [the single most sensory detail of the
story, mid-motion]. [SETTING implied by background blur]. Macro framing, very shallow depth
of field, slow push-in. Natural light: [source]. Mood: intrigue, warmth. Shot on ARRI Alexa
35, 100mm macro. No text, no logos. + [negatives]
```

### Scene 2 - Situation / context (4 s used)

Goal: the persona in their real life, a felt tension or desire.

```
Documentary style, hyperrealistic. [SUBJECT] [everyday action that shows the tension or
desire], in [SETTING]. Handheld camera at chest height, slight natural sway, point-of-view
distance of a family member. Natural light: [source, time of day]. Mood: [quiet tension /
longing / routine]. Fine textures: [details]. Shot on Sony FX3, 35mm. No text. + [negatives]
```

### Scene 3 - Transformation (4 s used)

Goal: the change happens on screen; the product/service appears as the enabler.

```
Documentary style, hyperrealistic. [SUBJECT or professional hands] [the concrete action of
change involving the product], in [same SETTING]. Slow confident camera move: [push-in or
orbit fragment], intimate framing on hands and faces. Natural light: [same source, slightly
brighter]. Mood: focus, capability, quiet pride. Fine textures: [material details of the
work]. Shot on ARRI Alexa 35, 35mm. No text. + [negatives]
```

### Scene 4 - Emotional close (2-6 s used)

Goal: the feeling after; face or posture at rest; room for the CTA text in edit.

```
Documentary style, hyperrealistic. [SUBJECT] [resting gesture: exhale, sip, lean back, small
smile not at camera], in [same SETTING]. Static or barely drifting camera, medium close-up,
generous negative space on [top/bottom] for captions. Natural light: golden hour glow. Mood:
[relief / calm / pride / joy], one emotion only. Shot on ARRI Alexa 35, 50mm. No text.
+ [negatives]
```

CTA is added in EDIT as subtitle-style text (no final period), never generated.

## 4. Continuity kit (same story across 4 clips)

Repeat verbatim in every prompt of one video:

- the SUBJECT description (word for word),
- the SETTING phrase,
- the LIGHT phrase,
- the grading tail ("real skin texture, natural color grading...").

Change only ACTION, framing and MOOD per scene. This is what makes 4 generations feel like
one film.

## 5. Per-tool cheat sheet (as of 2026, re-verify credits each session)

| Tool | Access | Quirks |
|---|---|---|
| Sora | ChatGPT Plus | Strong realism and physics. Likes full descriptive sentences. Generate 5-10 s, 9:16. Fold negatives into prompt text. |
| Grok (Imagine) | Works without X Premium | Fast, decent realism. Shorter prompts work better; keep the tech cue. |
| Meta AI | Free | Simplest; keep prompt to 2-3 sentences, lead with subject+action. |
| Kling (free tier) | Web, daily credits | Among the best free realism and motion. Has a negative-prompt field, use section 2 verbatim. Image-to-video good for continuity. |
| Hailuo / MiniMax (free tier) | Web credits | Good human motion. Keep moves simple, one per clip. |
| Veo via Gemini (free tier) | Google account | Good light and physics. Understands cinematographic vocabulary well. |
| Pika (free tier) | Web credits | Weaker realism; better for b-roll and textures than faces. |

Rules of thumb: faces and hands are the failure point everywhere, prefer hands-at-work and
three-quarter faces over frontal close-ups; regenerate a scene rather than accept a warped
hand; 9:16 at generation time (do not crop 16:9 later); pick the take with the most
believable MOTION, not the prettiest still frame.

## 6. Assembly after generation

1. Trim each clip to its arc length (2 / 4 / 4 / 2-6 s).
2. Plain cuts only; cut on the action.
3. Add ambient sound bed (free: freesound.org) and, if needed, quiet warm music.
4. Subtitles + one soft CTA end-line, safe zones respected, no final period, no em dashes.
5. Privacy pass: no readable plates, phones, faces of third parties (AI clips can still
   contain readable text artifacts, check).
6. Run the SKILL.md checklist; show the brand owner before publishing.
