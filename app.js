/**
 * STORY OF MY LIFE - Interactive Experience Engine
 * Features: Continuous Audio, Web Audio Synth, Pinterest Board, Attack Engine, 
 * Then-vs-Now Slider, Roast Cannon, Lightbox Modal
 */

(function () {
  'use strict';

  // --- Web Audio Sound Synthesizer ---
  let audioCtx = null;
  function getAudioContext() {
    if (!audioCtx) {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (AudioContextClass) audioCtx = new AudioContextClass();
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume().catch(() => {});
    }
    return audioCtx;
  }

  // Synthesize funny comic attack sound
  function playAttackSound() {
    try {
      const ctx = getAudioContext();
      if (!ctx) return;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      const sounds = ['boing', 'laser', 'punch', 'pop'];
      const chosen = sounds[Math.floor(Math.random() * sounds.length)];

      const now = ctx.currentTime;
      if (chosen === 'boing') {
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(160, now);
        osc.frequency.exponentialRampToValueAtTime(580, now + 0.12);
        osc.frequency.exponentialRampToValueAtTime(220, now + 0.28);
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.3);
      } else if (chosen === 'laser') {
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(950, now);
        osc.frequency.exponentialRampToValueAtTime(140, now + 0.2);
        gain.gain.setValueAtTime(0.25, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.2);
      } else if (chosen === 'punch') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.exponentialRampToValueAtTime(45, now + 0.18);
        gain.gain.setValueAtTime(0.4, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.2);
      } else {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(600, now);
        osc.frequency.exponentialRampToValueAtTime(1200, now + 0.1);
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.15);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.15);
      }
    } catch (e) {
      // Audio fallback silent
    }
  }

  // Synthesize sparkling chime sound for heart pin
  function playHeartChime() {
    try {
      const ctx = getAudioContext();
      if (!ctx) return;
      const notes = [523.25, 659.25, 783.99, 1046.50]; // C E G C
      const now = ctx.currentTime;
      notes.forEach((freq, i) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, now + i * 0.05);
        gain.gain.setValueAtTime(0.18, now + i * 0.05);
        gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.05 + 0.25);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now + i * 0.05);
        osc.stop(now + i * 0.05 + 0.25);
      });
    } catch (e) {}
  }

  // --- Confetti Engine ---
  function fireConfetti(originX, originY) {
    const colors = ['#F59E0B', '#E11D48', '#EC4899', '#8B5CF6', '#10B981', '#FBBF24'];
    const count = 28;
    for (let i = 0; i < count; i++) {
      const dot = document.createElement('div');
      dot.style.position = 'fixed';
      dot.style.left = (originX || window.innerWidth / 2) + 'px';
      dot.style.top = (originY || window.innerHeight / 2) + 'px';
      dot.style.width = Math.random() * 8 + 6 + 'px';
      dot.style.height = Math.random() * 8 + 6 + 'px';
      dot.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';
      dot.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
      dot.style.zIndex = '9999';
      dot.style.pointerEvents = 'none';

      const angle = Math.random() * Math.PI * 2;
      const distance = Math.random() * 260 + 80;
      const destX = Math.cos(angle) * distance;
      const destY = Math.sin(angle) * distance;

      dot.animate([
        { transform: 'translate(0, 0) scale(1) rotate(0deg)', opacity: 1 },
        { transform: `translate(${destX}px, ${destY}px) scale(0) rotate(${Math.random() * 720}deg)`, opacity: 0 }
      ], {
        duration: Math.random() * 600 + 800,
        easing: 'cubic-bezier(0.16, 1, 0.3, 1)'
      }).onfinish = () => dot.remove();

      document.body.appendChild(dot);
    }
  }

  // --- Continuous Audio Player Controller ---
  const bgAudio = document.getElementById('bgAudio');
  const btnAudioToggle = document.getElementById('btnAudioToggle');
  const audioBtnText = document.getElementById('audioBtnText');
  const lyricsMarquee = document.getElementById('lyricsMarquee');

  function updateAudioUI(playing) {
    if (!btnAudioToggle) return;
    if (playing) {
      btnAudioToggle.classList.remove('muted');
      if (audioBtnText) audioBtnText.textContent = '🎵 Music Playing';
    } else {
      btnAudioToggle.classList.add('muted');
      if (audioBtnText) audioBtnText.textContent = '🔇 Music Paused';
    }
  }

  function toggleAudio() {
    getAudioContext();
    if (!bgAudio) return;
    if (bgAudio.paused) {
      bgAudio.play().then(() => updateAudioUI(true)).catch(() => {});
    } else {
      bgAudio.pause();
      updateAudioUI(false);
    }
  }

  if (bgAudio) {
    bgAudio.volume = 0.85;
    bgAudio.addEventListener('play', () => updateAudioUI(true));
    bgAudio.addEventListener('pause', () => updateAudioUI(false));
  }

  if (btnAudioToggle) {
    btnAudioToggle.addEventListener('click', toggleAudio);
  }

  // Backup interaction listener to start music if autoplay was initially prevented
  const startMusicOnFirstTouch = () => {
    if (bgAudio && bgAudio.paused) {
      bgAudio.play().then(() => updateAudioUI(true)).catch(() => {});
    }
    window.removeEventListener('click', startMusicOnFirstTouch);
    window.removeEventListener('touchstart', startMusicOnFirstTouch);
  };
  window.addEventListener('click', startMusicOnFirstTouch);
  window.addEventListener('touchstart', startMusicOnFirstTouch);

  // Sync lyrics ticker
  if (lyricsMarquee && window.STORY_DATA && window.STORY_DATA.song) {
    const lyricsList = window.STORY_DATA.song.lyrics;
    let lyricIdx = 0;
    setInterval(() => {
      lyricIdx = (lyricIdx + 1) % lyricsList.length;
      lyricsMarquee.style.opacity = '0';
      setTimeout(() => {
        lyricsMarquee.textContent = `"${lyricsList[lyricIdx]}"`;
        lyricsMarquee.style.opacity = '1';
      }, 300);
    }, 6500);
  }

  // --- Entrance Gate Unlocking ---
  const gate = document.getElementById('gate');
  const btnOpenStory = document.getElementById('btnOpenStory');

  if (btnOpenStory && gate) {
    btnOpenStory.addEventListener('click', (e) => {
      getAudioContext();
      if (bgAudio) {
        bgAudio.volume = 0.85;
        bgAudio.play().then(() => {
          updateAudioUI(true);
        }).catch(() => {
          console.log('Autoplay deferred until user interaction');
        });
      }

      fireConfetti(e.clientX, e.clientY);
      gate.classList.add('hidden-gate');
      setTimeout(syncSliderDimensions, 300);
    });
  }

  // --- Interactive Then-vs-Now Slider (One Direction Style) ---
  const comparisonContainer = document.getElementById('comparisonContainer');
  const comparisonBefore = document.getElementById('comparisonBefore');
  const comparisonHandle = document.getElementById('comparisonHandle');

  let isDraggingSlider = false;

  function updateSliderPosition(clientX) {
    if (!comparisonContainer || !comparisonBefore || !comparisonHandle) return;
    const rect = comparisonContainer.getBoundingClientRect();
    let x = clientX - rect.left;
    if (x < 0) x = 0;
    if (x > rect.width) x = rect.width;

    const percent = (x / rect.width) * 100;
    comparisonBefore.style.width = percent + '%';
    comparisonHandle.style.left = percent + '%';

    const beforeImg = comparisonBefore.querySelector('img');
    if (beforeImg) {
      beforeImg.style.width = rect.width + 'px';
    }
  }

  function syncSliderDimensions() {
    if (!comparisonContainer || !comparisonBefore) return;
    const rect = comparisonContainer.getBoundingClientRect();
    const beforeImg = comparisonBefore.querySelector('img');
    if (beforeImg) {
      beforeImg.style.width = rect.width + 'px';
    }
  }

  window.addEventListener('resize', syncSliderDimensions);
  setTimeout(syncSliderDimensions, 100);

  if (comparisonContainer) {
    comparisonContainer.addEventListener('mousedown', (e) => {
      isDraggingSlider = true;
      updateSliderPosition(e.clientX);
    });

    window.addEventListener('mousemove', (e) => {
      if (isDraggingSlider) updateSliderPosition(e.clientX);
    });

    window.addEventListener('mouseup', () => {
      isDraggingSlider = false;
    });

    comparisonContainer.addEventListener('touchstart', (e) => {
      isDraggingSlider = true;
      if (e.touches.length > 0) updateSliderPosition(e.touches[0].clientX);
    }, { passive: true });

    window.addEventListener('touchmove', (e) => {
      if (isDraggingSlider && e.touches.length > 0) updateSliderPosition(e.touches[0].clientX);
    }, { passive: true });

    window.addEventListener('touchend', () => {
      isDraggingSlider = false;
    });
  }

  // --- Pinterest Masonry Board Renderer ---
  const pinterestGrid = document.getElementById('pinterestGrid');
  const allItems = (window.STORY_DATA ? window.STORY_DATA.items : []).concat(
    window.STORY_DATA && window.STORY_DATA.videos ? window.STORY_DATA.videos : []
  );

  let currentEraFilter = 'all';
  let currentVibeFilter = 'all';

  const ATTACK_BURSTS = [
    'EMOTIONAL DAMAGE! 💀',
    'AURA +10,000 ✨',
    'CRIMINAL SIDE-EYE 👀',
    'CAUGHT IN 4K 📸',
    'SLAY OF THE CENTURY 👑',
    'MAIN CHARACTER ALERT 🚨',
    'FACE CARD NEVER DECLINES 💳',
    'HELLO KITTY CERTIFIED 🎀',
    'UNBOTHERED QUEEN 💅',
    'SNACK EXPEDITION K.O. 🍕'
  ];

  function renderGrid() {
    if (!pinterestGrid) return;
    pinterestGrid.innerHTML = '';

    const filtered = allItems.filter(item => {
      const matchEra = (currentEraFilter === 'all') || (item.eraKey === currentEraFilter);
      const matchVibe = (currentVibeFilter === 'all') || (item.vibe === currentVibeFilter);
      return matchEra && matchVibe;
    });

    if (filtered.length === 0) {
      pinterestGrid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 60px 20px; color: #827A71;">
          <h3 style="font-size: 1.5rem; margin-bottom: 8px;">No memories found for this vibe</h3>
          <p>Try switching to another chapter or reset the filter!</p>
        </div>
      `;
      return;
    }

    filtered.forEach((item, index) => {
      const card = document.createElement('article');
      card.className = 'pin-card';
      card.setAttribute('data-id', item.id);
      card.setAttribute('data-index', index);

      // Media markup (photo vs video)
      let mediaMarkup = '';
      if (item.isVideo) {
        mediaMarkup = `
          <div class="pin-media-wrap">
            <video class="pin-video" src="${encodeURI(item.src)}" preload="metadata" muted playsinline loop></video>
            <div class="video-badge">▶ Video</div>
            <div class="pin-overlay-actions">
              <button class="btn-pin-heart" title="Save to Board" aria-label="Save to Board">♥</button>
            </div>
          </div>
        `;
      } else {
        mediaMarkup = `
          <div class="pin-media-wrap">
            <img class="pin-image" src="${encodeURI(item.src)}" alt="${item.title}" loading="lazy" />
            <div class="pin-overlay-actions">
              <button class="btn-pin-heart" title="Save to Board" aria-label="Save to Board">♥</button>
            </div>
          </div>
        `;
      }

      // Card structure
      card.innerHTML = `
        <div class="washi-tape"></div>
        <div class="push-pin"></div>
        ${mediaMarkup}
        <div class="pin-body">
          <div class="pin-era-meta">
            <span class="pin-era-tag">${item.eraName}</span>
            <span class="pin-vibe-badge">${item.vibe.toUpperCase()}</span>
          </div>
          <h3 class="pin-title">${item.title}</h3>
          <p class="pin-caption">${item.caption}</p>
          <div class="pin-expression-box">
            <div class="expression-title">🔍 Expression Radar</div>
            <div class="expression-desc">"${item.expression}"</div>
          </div>
          <div class="pin-attack-bar">
            <button class="btn-card-attack" type="button">
              ⚡ ATTACK!
            </button>
            <span class="attack-stat-count">Hits: <b class="hit-count">0</b></span>
          </div>
          <div class="pin-tags">
            ${item.tags ? item.tags.map(t => `<span class="pin-tag-chip">${t}</span>`).join('') : ''}
          </div>
        </div>
      `;

      // Auto-play videos on card hover
      if (item.isVideo) {
        const vid = card.querySelector('video');
        if (vid) {
          card.addEventListener('mouseenter', () => vid.play().catch(() => {}));
          card.addEventListener('mouseleave', () => {
            vid.pause();
            vid.currentTime = 0;
          });
        }
      }

      // Attack Button Interactive Launcher
      const btnAttack = card.querySelector('.btn-card-attack');
      const hitDisplay = card.querySelector('.hit-count');
      let hitCount = 0;

      btnAttack.addEventListener('click', (e) => {
        e.stopPropagation();
        hitCount++;
        hitDisplay.textContent = hitCount;
        playAttackSound();

        // Card wobble shake animation
        card.classList.remove('card-shaking');
        void card.offsetWidth; // Trigger reflow
        card.classList.add('card-shaking');

        // Spawn dynamic sticker burst over card
        const sticker = document.createElement('div');
        sticker.className = 'attack-sticker-burst';
        const randomAttack = ATTACK_BURSTS[Math.floor(Math.random() * ATTACK_BURSTS.length)];
        sticker.textContent = randomAttack;
        card.appendChild(sticker);
        setTimeout(() => sticker.remove(), 1250);
      });

      // Pin Heart Favorite Button
      const btnHeart = card.querySelector('.btn-pin-heart');
      btnHeart.addEventListener('click', (e) => {
        e.stopPropagation();
        playHeartChime();

        // Floating heart physics
        const heart = document.createElement('div');
        heart.className = 'floating-heart';
        heart.textContent = '❤️';
        heart.style.left = e.clientX + 'px';
        heart.style.top = e.clientY + 'px';
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), 1400);
      });

      // Click card to open modal lightbox
      card.addEventListener('click', () => {
        openModal(item, filtered);
      });

      pinterestGrid.appendChild(card);
    });
  }

  // --- Lightbox Modal Engine ---
  const modalBackdrop = document.getElementById('modalBackdrop');
  const btnCloseModal = document.getElementById('btnCloseModal');
  const modalMediaWrap = document.getElementById('modalMediaWrap');
  const modalEraBadge = document.getElementById('modalEraBadge');
  const modalTitle = document.getElementById('modalTitle');
  const modalCaption = document.getElementById('modalCaption');
  const modalExpText = document.getElementById('modalExpText');
  const btnModalPrev = document.getElementById('btnModalPrev');
  const btnModalNext = document.getElementById('btnModalNext');

  let currentModalIndex = 0;
  let activeModalList = [];

  function openModal(item, list) {
    if (!modalBackdrop) return;
    activeModalList = list || allItems;
    currentModalIndex = activeModalList.findIndex(x => x.id === item.id);
    if (currentModalIndex === -1) currentModalIndex = 0;
    renderModalItem(activeModalList[currentModalIndex]);
    modalBackdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    if (!modalBackdrop) return;
    modalBackdrop.classList.remove('active');
    document.body.style.overflow = '';
    // Pause any playing modal video
    const vid = modalMediaWrap.querySelector('video');
    if (vid) vid.pause();
  }

  function renderModalItem(item) {
    if (!item) return;
    if (item.isVideo) {
      modalMediaWrap.innerHTML = `<video class="modal-video" src="${encodeURI(item.src)}" controls autoplay playsinline loop></video>`;
    } else {
      modalMediaWrap.innerHTML = `<img class="modal-img" src="${encodeURI(item.src)}" alt="${item.title}" />`;
    }

    modalEraBadge.textContent = item.eraName;
    modalTitle.textContent = item.title;
    modalCaption.textContent = item.caption;
    modalExpText.textContent = `"${item.expression}"`;
  }

  if (btnCloseModal) btnCloseModal.addEventListener('click', closeModal);
  if (modalBackdrop) {
    modalBackdrop.addEventListener('click', (e) => {
      if (e.target === modalBackdrop) closeModal();
    });
  }

  if (btnModalPrev) {
    btnModalPrev.addEventListener('click', () => {
      if (activeModalList.length === 0) return;
      currentModalIndex = (currentModalIndex - 1 + activeModalList.length) % activeModalList.length;
      renderModalItem(activeModalList[currentModalIndex]);
    });
  }

  if (btnModalNext) {
    btnModalNext.addEventListener('click', () => {
      if (activeModalList.length === 0) return;
      currentModalIndex = (currentModalIndex + 1) % activeModalList.length;
      renderModalItem(activeModalList[currentModalIndex]);
    });
  }

  window.addEventListener('keydown', (e) => {
    if (!modalBackdrop.classList.contains('active')) return;
    if (e.key === 'Escape') closeModal();
    if (e.key === 'ArrowLeft' && btnModalPrev) btnModalPrev.click();
    if (e.key === 'ArrowRight' && btnModalNext) btnModalNext.click();
  });

  // --- Pinterest Filter Tab Listeners ---
  const filterTabs = document.querySelectorAll('.filter-tab');
  filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      filterTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      currentEraFilter = tab.getAttribute('data-era');
      renderGrid();
    });
  });

  const vibePills = document.querySelectorAll('.vibe-pill');
  vibePills.forEach(pill => {
    pill.addEventListener('click', () => {
      vibePills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      currentVibeFilter = pill.getAttribute('data-vibe');
      renderGrid();
    });
  });

  // Top Nav Chapter Jump Buttons
  const navChapterBtns = document.querySelectorAll('.chapter-nav-btn');
  navChapterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const eraKey = btn.getAttribute('data-era');
      navChapterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Sync filter tab
      const matchingTab = document.querySelector(`.filter-tab[data-era="${eraKey}"]`);
      if (matchingTab) {
        filterTabs.forEach(t => t.classList.remove('active'));
        matchingTab.classList.add('active');
        currentEraFilter = eraKey;
        renderGrid();
      }

      // Smooth scroll to timeline section
      const targetSec = document.getElementById('gallerySection');
      if (targetSec) {
        targetSec.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // Initial Grid Render
  renderGrid();

})();
