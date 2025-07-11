---
title: Press Release - WeStory.ai Transforms Personal Storytelling Through AI-Powered Biography Creation
date: Tue Jan 14 19:03:10 PST 2025
last_modified_at: Sat Jul 12 02:05:17 PDT 2025
categories:
 - pr&faq
tags:
 - business
 - startup
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
---

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

# NotebookLM Podcasts

<audio id="podcast-1" controls>
	<source type="audio/wav" src="/resource/posts/2025-01-14-PST - Press Release - WeStory/NotebookLM/WeStory_ai_ AI Transforms Personal Storytelling and Legacy Creation-01.wav">
	Your browser does not support this shorter audio element.
</audio>

# Press Release

December 1, 2025

Cupertino, CA – WeStory.ai today announced groundbreaking achievements in AI-powered personal storytelling, helping hundreds of individuals preserve their life stories through an innovative interview-based platform. The company's technology, powered by advanced language models like ChatGPT and Claude, conducts personalized interviews that capture and preserve individual and family narratives in unprecedented detail.

"At WeStory.ai, we believe in the power of stories to revive and celebrate lives," said Juyong Do, CEO of WeStory.ai. "Our AI agents have helped many, especially the elderly, realize the value of their life stories, leaving a meaningful legacy for future generations."

<div class="img-container">
<img style="max-width: 70%;" src="/assets/images/we-story-ai/grandma.png">
</div>

The platform's unique approach enables users to engage in natural conversations with AI agents that act as personal biographers, carefully crafting narratives that capture life experiences.
WeStory.ai's technology can independently interview multiple family members, weaving together separate accounts into comprehensive family histories that bridge generational gaps.

<!--div class="callout"-->
<blockquote>
@Juyong I want to add more feature in this paragraph!
</blockquote>
<!--/div-->

<div class="img-container">
<img style="max-width: 70%;" src="/assets/images/we-story-ai/family.png">
</div>

The platform's impact has been significant across multiple dimensions. WeStory.ai has helped over 500 individuals publish their stories as Amazon e-books, while facilitating the creation of 135 physical books. The company's innovative approach has resonated strongly in the market, generating $500,000 in revenue over the past year and securing $2.5 million in recurring revenue contracts. These achievements have been complemented by strategic partnerships with nonprofit organizations, including K-Diaspora, extending the platform's reach and impact.

<div class="img-container">
<img style="max-width: 70%;" src="/assets/images/we-story-ai/books.png">
</div>

"Writing my story with WeStory.ai made me realize how meaningful my life has been," shared a customer. "I now have a legacy to leave behind for my children and grandchildren."

Financially, WeStory.ai has generated $500,000 in revenue over the past year and has secured contracts ensuring $2.5 million in recurring revenue moving forward.
The company has also started donating a portion of its earnings to nonprofit organizations like the K-Diaspora and other like-minded groups, reinforcing its commitment to societal impact.

<div class="img-container">
<img style="max-width: 70%;" src="/assets/images/we-story-ai/money.png">
</div>

Building on its success in personal storytelling, WeStory.ai has expanded its social impact through partnerships with organizations like K-Diaspora, helping preserve important cultural narratives. The company also dedicates a portion of its earnings to support nonprofit organizations aligned with its mission of connecting generations through storytelling.

Looking ahead, WeStory.ai plans to venture into AI-generated movie scenarios, furthering its mission to bridge technological gaps and foster meaningful human connections through innovative storytelling solutions.

For more information, visit <a href="https://westory.ai/">WeStory.ai</a>.

<script>
// Function to get URL parameters
function getUrlParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Function to auto-play audio based on URL parameter
function autoPlayAudio() {
    const audioParam = getUrlParameter('audio');
    if (audioParam) {
        const audioElement = document.getElementById(audioParam);
        if (audioElement) {
            // Scroll to the audio element
            audioElement.scrollIntoView({ behavior: 'smooth', block: 'center' });

            // Add a small delay to ensure the page has loaded
            setTimeout(() => {
                audioElement.play().catch(error => {
                    console.log('Auto-play was prevented by browser:', error);
                    // Highlight the audio element if auto-play fails
                    audioElement.style.border = '3px solid #ff6b6b';
                    audioElement.style.borderRadius = '5px';
                });
            }, 500);
			// Alternative: Simulate click on play button
			/*
			setTimeout(() => {
				audioElement.play().catch(error => {
					// If auto-play fails, show a prominent play button or notification
					const playButton = document.createElement('button');
					playButton.textContent = '▶ Click to Play Selected Audio';
					playButton.style.cssText = `
						position: fixed;
						top: 20px;
						right: 20px;
						z-index: 1000;
						background: #007cba;
						color: white;
						border: none;
						padding: 10px 20px;
						border-radius: 5px;
						cursor: pointer;
						font-size: 16px;
					`;
					playButton.onclick = () => {
						audioElement.play();
						document.body.removeChild(playButton);
					};
					document.body.appendChild(playButton);
				});
			}, 500);
			*/
        }
    }
}

// Run the function when the page loads
document.addEventListener('DOMContentLoaded', autoPlayAudio);
</script>
