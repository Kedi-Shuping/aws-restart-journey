# Sootheum

*A learning app developed to support my daughter's speech development through voice-powered activities, narrated stories, and emotional-regulation tools.*

**[Explore the live app](https://d1m0wbmmfzbc8z.cloudfront.net)**

Six storybooks · Five voice games · Recorded narration · Calm Corner

---

## Overview

Sootheum is a single-file web app built around interactive learning and emotional regulation. It includes six storybooks, five voice games, a Calm Corner, and a custom **Mommy's Voice** feature. Across the six books, 126 pages have recorded narration, allowing stories to be read in a familiar voice.

The app was developed incrementally over several months, guided by what worked in practice.

## The Problem

Several features rely on live microphone input, including a game where a flower grows as the child speaks affirmations, a recording studio with playback and audio effects, and a sequencing game that listens for spoken steps.

During testing, microphone access failed even when permission appeared to be granted. The app's fallback behaviour could activate instead—for example, the flower game offered tapping rather than responding to voice.

## Diagnosis

The app was initially served from an Amazon S3 static website endpoint over HTTP. Browser microphone APIs such as `navigator.mediaDevices.getUserMedia()` require a **secure context**. In general, browsers allow these APIs on HTTPS origins and on certain trusted development origins, such as `http://localhost`.

An ordinary HTTP website does not meet that requirement. As a result, the browser can make microphone access unavailable or reject a request, regardless of whether the site's microphone permission appears to have been granted.

The investigation pointed to the serving environment rather than an application-code change.

## The Solution

I placed the site behind **Amazon CloudFront**, which provides an HTTPS endpoint for visitors. This put the deployed app in a secure context so its microphone-dependent features could request access to the browser's media APIs.

The fix was architectural: no application code change was needed to resolve this particular deployment issue.

CloudFront also provides edge caching for static content, which can help reduce latency and repeated requests to the origin.

## Architecture

The deployment uses CloudFront in front of an Amazon S3 static website origin:

```text
Browser
   │
   │ HTTPS
   ▼
Amazon CloudFront
   │
   │ HTTP to S3 website endpoint
   ▼
Amazon S3 static website
   ├── index.html
   ├── sounds/   (narration, ambient and comfort audio)
   └── images/   (scene backgrounds and interface artwork)
```

**Connection note:** HTTPS protects the visitor-to-CloudFront connection. When CloudFront uses an S3 *website endpoint* as its origin, the CloudFront-to-origin connection uses HTTP. The two connections are separate.

## AWS Services and Browser APIs

- **Amazon S3** — static website origin
- **Amazon CloudFront** — HTTPS delivery and content distribution
- **Web Audio API** — real-time microphone amplitude analysis
- **MediaRecorder API** — voice recording and playback

## Implementation Notes

### Recorded narration and fallback

Story pages use recorded narration where an audio file is available. If a narration file is not available for a page, the reader falls back to the browser's native text-to-speech API.

### Voice sensitivity

The Voice Power game analyses microphone input in real time using the Web Audio API. It smooths the amplitude signal with a moving average across several frames, helping the game respond to sustained vocal input rather than a single brief spike.

The sensitivity threshold is configurable and was tuned during testing for the intended use case. A threshold value is meaningful only in the context of the app's amplitude calculation and should not be treated as a universal setting for other microphones or environments.

## Verification

During testing:

- Microphone input was captured after the app was deployed behind CloudFront.
- The Voice Power game responded to live voice input.
- Voice recording and playback worked in a secure context.
- The text-to-speech fallback was checked on a story page without a narration file.
- The live app was opened and checked on desktop and mobile.

These checks document the behaviours tested; they are not a claim that every feature has been exhaustively tested across every device or browser.

## Screenshots

### Home

![Sootheum home screen](Screenshots/01-home.png)

### Voice Power

The flower grows as the child speaks affirmations, using real-time microphone analysis.

![Voice Power game](Screenshots/02-voice-power.png)

### Story Library

Six original storybooks developed around speech and emotional milestones.

![Story library](Screenshots/03-story-library.png)

### My Voice

Guided practice (**Say It with Me**) and open recording (**Your Turn to Talk**).

![My Voice screen](Screenshots/04-my-voice.png)

### Calm Corner

Regulation tools include a breathing guide, glitter jar, ambient nature sounds, and a recording of the child's mother's voice for comfort.

![Calm Corner](Screenshots/05-calm-corner.png)

---

## What This Project Demonstrates

- **Browser security:** recognising that microphone access depends on secure-context requirements.
- **Cloud architecture:** serving a static S3 website through CloudFront to provide HTTPS to visitors.
- **Troubleshooting:** distinguishing an application-code issue from a deployment-environment constraint.
- **Accessible interaction design:** combining voice interaction, recorded narration, browser text-to-speech, and emotional-regulation activities.

---

*Built around a child's learning and communication journey.*
