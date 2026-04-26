// ============================================================
//  main.js — SkinSight · Frontend Logic
//  Mengelola pilihan gejala & komunikasi dengan Flask API
// ============================================================

const selected = new Set();

// ── Toggle pilihan gejala ─────────────────────────────────────
function toggle(el) {
  const id = el.dataset.id;
  el.classList.toggle("selected");
  if (selected.has(id)) {
    selected.delete(id);
  } else {
    selected.add(id);
  }
}

// ── Kirim ke API & tampilkan hasil ───────────────────────────
async function diagnose() {
  if (selected.size < 2) {
    const alert = document.getElementById("alertWarn");
    alert.classList.add("show");
    setTimeout(() => alert.classList.remove("show"), 3000);
    return;
  }

  const btn = document.getElementById("btnDiagnose");
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner"></span>Menganalisis...';

  try {
    const res = await fetch("/api/diagnose", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ symptoms: Array.from(selected) }),
    });

    if (!res.ok) throw new Error("Server error: " + res.status);

    const data = await res.json();
    if (data.error) throw new Error(data.error);

    renderResult(data);

  } catch (err) {
    alert("Terjadi kesalahan: " + err.message);
  } finally {
    btn.disabled = false;
    btn.innerHTML = "Mulai Analisis → Diagnosis";
  }
}

// ── Render hasil ke DOM ───────────────────────────────────────
function renderResult(data) {
  // Step bar
  setStepDone(1); setStepDone(2); setStepActive(3);

  // Hero
  document.getElementById("resultTitle").textContent    = data.name;
  document.getElementById("resultSubtitle").textContent = data.subtitle;
  document.getElementById("confNum").textContent        = data.confidence + "%";
  setTimeout(() => {
    document.getElementById("confBar").style.width = data.confidence + "%";
  }, 200);

  // Diagnosis cards
  document.getElementById("diagGrid").innerHTML = data.cards
    .map(c => `
      <div class="diag-card">
        <div class="diag-card-icon">${c.icon}</div>
        <div class="diag-card-title">${c.title}</div>
        <div class="diag-card-body">${c.body}</div>
      </div>`)
    .join("");

  // Ingredients
  document.getElementById("goodIngredients").innerHTML = data.ingredients_good
    .map(i => `<span class="tag good">${i}</span>`).join("");
  document.getElementById("badIngredients").innerHTML = data.ingredients_bad
    .map(i => `<span class="tag bad">${i}</span>`).join("");

  // Routine
  document.getElementById("routineSteps").innerHTML = data.routine
    .map((r, i) => `
      <div class="routine-step">
        <div class="routine-num">${String(i + 1).padStart(2, "0")}</div>
        <div>
          <div class="routine-name">${r.step}</div>
          <div class="routine-desc">${r.desc}</div>
        </div>
      </div>`)
    .join("");

  // Rule trace
  const rules = data.fired_rules;
  document.getElementById("traceRules").innerHTML = rules.length > 0
    ? rules.map(r => `
        <div class="trace-rule">
          <span class="trace-rule-id">${r.rule_id}</span>
          <span class="trace-rule-text">${
            r.desc
              .replace("IF ",    "<strong>IF</strong> ")
              .replace(" AND ",  " <strong>AND</strong> ")
              .replace(" THEN ", " <strong>THEN</strong> ")
          }</span>
        </div>`)
      .join("")
    : `<div class="trace-rule">
         <span class="trace-rule-id">R?</span>
         <span class="trace-rule-text">Diagnosis berdasarkan kombinasi gejala yang dipilih.</span>
       </div>`;

  // Tampilkan hasil & sembunyikan input
  document.getElementById("inputSection").style.display = "none";
  document.getElementById("resultSection").classList.add("visible");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// ── Reset ─────────────────────────────────────────────────────
function reset() {
  selected.clear();
  document.querySelectorAll(".symptom-item").forEach(el => el.classList.remove("selected"));
  document.getElementById("resultSection").classList.remove("visible");
  document.getElementById("confBar").style.width = "0%";
  document.getElementById("inputSection").style.display = "block";
  setStepActive(1); setStepDefault(2); setStepDefault(3);
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// ── Step bar helpers ──────────────────────────────────────────
function setStepActive(n) {
  document.getElementById("dot" + n).className  = "step-dot active";
  document.getElementById("lbl" + n).className  = "step-label active";
}
function setStepDone(n) {
  document.getElementById("dot" + n).className  = "step-dot done";
  document.getElementById("lbl" + n).className  = "step-label";
}
function setStepDefault(n) {
  document.getElementById("dot" + n).className  = "step-dot";
  document.getElementById("lbl" + n).className  = "step-label";
}
