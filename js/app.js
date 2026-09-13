(() => {
  const data = window.ADMISSIONS_DATA;
  if (!data) {
    document.body.innerHTML = "<p style='padding:24px'>缺少 js/data.js，请先运行 build_data.py</p>";
    return;
  }

  const REGION_LABEL = { HK: "香港", SG: "新加坡", US: "美国" };
  const REGION_ACTIVE = { HK: "active-hk", SG: "active-sg", US: "active-us" };

  const state = {
    region: "HK",
    degree: "PhD",
    query: "",
    campus: "All",
    funding: "All",
    sort: "rank",
    selectedId: null,
  };

  const $ = (id) => document.getElementById(id);
  const title = $("title");
  const subtitle = $("subtitle");
  const stats = $("stats");
  const hkpfs = $("hkpfs");
  const singaEl = $("singa");
  const list = $("list");
  const detail = $("detail");
  const count = $("count");
  const footer = $("footer");
  const campusWrap = $("campusFilterWrap");

  title.textContent = data.meta.title;
  subtitle.textContent = data.meta.subtitle + " · 生成于 " + data.meta.generated;

  const all = data.programs;
  const hkN = all.filter((p) => p.region === "HK").length;
  const usN = all.filter((p) => p.region === "US").length;
  const sgN = all.filter((p) => p.region === "SG").length;
  const phdN = all.filter((p) => p.degreeGroup === "PhD").length;
  const msN = all.filter((p) => p.degreeGroup === "Master").length;
  const mainlandN = all.filter((p) => p.campusType === "mainland").length;

  stats.innerHTML = [
    ["收录条目", all.length],
    ["香港", `${hkN}（内地 ${mainlandN}）`],
    ["新加坡", sgN],
    ["美国", usN],
    ["PhD / 硕士", `${phdN} / ${msN}`],
  ]
    .map(([label, val]) => `<div class="stat"><b>${val}</b><span>${label}</span></div>`)
    .join("");

  const h = data.meta.hkpfs;
  hkpfs.innerHTML = `<strong>HKPFS 2027/28（仅香港本校 PhD）</strong><br/>
    津贴 ${h.stipend} + 旅费 ${h.travel} · ${h.awards} 个名额<br/>
    RGC 截止 ${h.rgcDeadline}；八校完整申请 ${h.uniDeadline}<br/>
    <a href="${h.portal}" target="_blank" rel="noopener">官方门户</a> · ${h.note}`;

  if (data.meta.singa && singaEl) {
    const s = data.meta.singa;
    singaEl.innerHTML = `<strong>SINGA（新加坡国际博士奖学金）</strong><br/>
      ${s.intake} 截止 ${s.deadline}<br/>
      <a href="${s.portal}" target="_blank" rel="noopener">SINGA 官方页</a> · ${s.note}`;
  }

  footer.innerHTML = `<strong>免责声明</strong>：${data.meta.disclaimer}<br/><strong>主要来源</strong>：${data.meta.sources.join(
    " · "
  )}`;

  function regionClass(r) {
    if (r === "HK") return "hk";
    if (r === "SG") return "sg";
    return "us";
  }

  function filtered() {
    let rows = all.filter((p) => p.region === state.region && p.degreeGroup === state.degree);
    if (state.region === "HK" && state.campus !== "All") {
      rows = rows.filter((p) => p.campusType === state.campus);
    }
    if (state.funding !== "All") rows = rows.filter((p) => p.funding === state.funding);
    if (state.query.trim()) {
      const q = state.query.trim().toLowerCase();
      rows = rows.filter((p) =>
        [p.school, p.schoolFull, p.field, p.degree, p.notes, p.fundingDetail, p.location || "", p.state || ""]
          .join(" ")
          .toLowerCase()
          .includes(q)
      );
    }
    rows.sort((a, b) => {
      if (state.sort === "deadline") return String(a.deadline).localeCompare(String(b.deadline));
      if (state.sort === "name") return a.school.localeCompare(b.school);
      const ra = a.rankBand || 999;
      const rb = b.rankBand || 999;
      if (ra !== rb) return ra - rb;
      return a.school.localeCompare(b.school);
    });
    return rows;
  }

  function fundingLabel(f) {
    if (f === "full") return "典型全奖";
    if (f === "partial") return "部分资助";
    return "自费为主";
  }

  function renderList() {
    campusWrap.style.display = state.region === "HK" ? "block" : "none";
    const rows = filtered();
    count.textContent = `当前显示 ${rows.length} 条 · ${REGION_LABEL[state.region]} · ${
      state.degree === "PhD" ? "PhD" : "硕士"
    }`;

    if (!rows.length) {
      list.innerHTML = `<div class="empty">没有匹配结果，请放宽筛选</div>`;
      detail.innerHTML = `<div class="empty">没有匹配项目</div>`;
      return;
    }

    if (!state.selectedId || !rows.find((r) => r.id === state.selectedId)) {
      state.selectedId = rows[0].id;
    }

    list.innerHTML = rows
      .map((p) => {
        const selected = p.id === state.selectedId ? "selected" : "";
        const rc = regionClass(p.region);
        const rank = p.rankBand != null ? `<span class="pill">USN≈#${p.rankBand}</span>` : "";
        const campus =
          p.campusType === "mainland"
            ? `<span class="pill mainland">内地分校</span>`
            : p.region === "HK"
            ? `<span class="pill hk">香港本校</span>`
            : p.region === "SG"
            ? `<span class="pill sg">新加坡</span>`
            : "";
        return `<article class="card ${rc} ${selected}" data-id="${p.id}">
          <div class="card-top">
            <div>
              <h3>${p.school} · ${p.degree}</h3>
              <div class="meta">${p.field}${p.location ? " · " + p.location : ""}${
          p.state ? " · " + p.state : ""
        }</div>
            </div>
            <div class="meta">${p.deadline}</div>
          </div>
          <div class="pills">
            <span class="pill ${rc}">${REGION_LABEL[p.region]}</span>
            <span class="pill ${p.degreeGroup === "PhD" ? "phd" : "master"}">${p.degreeGroup}</span>
            <span class="pill ${p.funding === "full" ? "full" : "self"}">${fundingLabel(p.funding)}</span>
            ${campus}${rank}
          </div>
        </article>`;
      })
      .join("");

    list.querySelectorAll(".card").forEach((el) => {
      el.addEventListener("click", () => {
        state.selectedId = el.getAttribute("data-id");
        render();
      });
    });

    renderDetail(rows.find((r) => r.id === state.selectedId));
  }

  function renderDetail(p) {
    if (!p) {
      detail.innerHTML = `<div class="empty">请选择项目</div>`;
      return;
    }
    detail.className =
      "panel detail " +
      (p.region === "HK" ? "region-hk" : p.region === "SG" ? "region-sg" : "region-us");

    const campusLine =
      p.campusType === "mainland"
        ? `<span class="pill mainland">内地分校 / 合作校区</span>`
        : p.region === "HK"
        ? `<span class="pill hk">香港本校</span>`
        : p.region === "SG"
        ? `<span class="pill sg">新加坡</span>`
        : `<span class="pill us">${p.state || "USA"}</span>`;

    detail.innerHTML = `
      <div class="pills" style="margin-bottom:8px">
        ${campusLine}
        <span class="pill ${p.degreeGroup === "PhD" ? "phd" : "master"}">${p.degree}</span>
        <span class="pill ${p.funding === "full" ? "full" : "self"}">${fundingLabel(p.funding)}</span>
      </div>
      <h2>${p.schoolFull || p.school}</h2>
      <div class="sub">${p.field} · ${p.entry}</div>
      <div class="kv">
        <b>申请开放</b><span>${p.opens || "—"}</span>
        <b>截止日期</b><span>${p.deadline}${p.deadlineNote ? "（" + p.deadlineNote + "）" : ""}</span>
        <b>Funding</b><span>${p.fundingDetail}</span>
        <b>GRE</b><span>${p.gre}</span>
        <b>英语</b><span>${p.english}</span>
        ${
          p.rankBand != null
            ? `<b>排名参考</b><span>约 US News Grad CS #${p.rankBand} 档 · ${p.rankSource || ""}</span>`
            : ""
        }
      </div>
      <section>
        <h4>招生要求</h4>
        <ul>${(p.requirements || []).map((x) => `<li>${x}</li>`).join("")}</ul>
      </section>
      <section>
        <h4>材料清单</h4>
        <ul>${(p.materials || []).map((x) => `<li>${x}</li>`).join("")}</ul>
      </section>
      <section>
        <h4>备注</h4>
        <p style="margin:0;line-height:1.5">${p.notes || ""}</p>
      </section>
      <div class="links">
        <a href="${p.applyUrl}" target="_blank" rel="noopener">注册 / 申请系统</a>
        <a href="${p.infoUrl}" target="_blank" rel="noopener" style="opacity:.9">项目说明页</a>
      </div>
    `;
  }

  function render() {
    renderList();
  }

  document.querySelectorAll("#regionTabs .tab").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.region = btn.getAttribute("data-region");
      document.querySelectorAll("#regionTabs .tab").forEach((b) => {
        b.className = "tab";
        const r = b.getAttribute("data-region");
        if (r === state.region) b.classList.add(REGION_ACTIVE[r]);
      });
      state.selectedId = null;
      render();
    });
  });

  document.querySelectorAll("#degreeTabs .tab").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.degree = btn.getAttribute("data-degree");
      document.querySelectorAll("#degreeTabs .tab").forEach((b) => {
        b.className = "tab";
        if (b.getAttribute("data-degree") === state.degree) {
          b.classList.add(state.degree === "PhD" ? "active-phd" : "active-master");
        }
      });
      state.selectedId = null;
      render();
    });
  });

  $("q").addEventListener("input", (e) => {
    state.query = e.target.value;
    render();
  });
  $("campus").addEventListener("change", (e) => {
    state.campus = e.target.value;
    render();
  });
  $("funding").addEventListener("change", (e) => {
    state.funding = e.target.value;
    render();
  });
  $("sort").addEventListener("change", (e) => {
    state.sort = e.target.value;
    render();
  });

  render();
})();
