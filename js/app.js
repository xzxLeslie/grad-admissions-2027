(() => {
  const data = window.ADMISSIONS_DATA;
  if (!data) {
    document.body.innerHTML = "<p style='padding:24px'>缺少 js/data.js，请先运行 build_data.py</p>";
    return;
  }

  const REGION_LABEL = { HK: "香港", SG: "新加坡", US: "美国" };
  const REGION_ACTIVE = { HK: "active-hk", SG: "active-sg", US: "active-us" };
  const SCHOOL_REGION = {};
  data.programs.forEach((p) => {
    if (!SCHOOL_REGION[p.school]) SCHOOL_REGION[p.school] = p.region;
  });

  const state = {
    region: "HK",
    degree: "PhD",
    query: "",
    campus: "All",
    funding: "All",
    sort: "rank",
    selectedId: null,
    selectedFacultyKey: null,
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
  const faculty = data.faculty || { directories: {}, highlights: [], disclaimer: "" };
  const hkN = all.filter((p) => p.region === "HK").length;
  const usN = all.filter((p) => p.region === "US").length;
  const sgN = all.filter((p) => p.region === "SG").length;
  const phdN = all.filter((p) => p.degreeGroup === "PhD").length;
  const msN = all.filter((p) => p.degreeGroup === "Master").length;
  const mainlandN = all.filter((p) => p.campusType === "mainland").length;
  const dirN = Object.keys(faculty.directories || {}).length;
  const hiN = (faculty.highlights || []).length;

  stats.innerHTML = [
    ["收录条目", all.length],
    ["香港", `${hkN}（内地 ${mainlandN}）`],
    ["新加坡", sgN],
    ["美国", usN],
    ["教师名录/重点导师", `${dirN} / ${hiN}`],
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

  footer.innerHTML = `<strong>免责声明</strong>：${data.meta.disclaimer}<br/>
    <strong>老师信息</strong>：${faculty.disclaimer || ""}<br/>
    <strong>主要来源</strong>：${data.meta.sources.join(" · ")}`;

  function regionClass(r) {
    if (r === "HK") return "hk";
    if (r === "SG") return "sg";
    return "us";
  }

  function fundingLabel(f) {
    if (f === "full") return "典型全奖";
    if (f === "partial") return "部分资助";
    return "自费为主";
  }

  function schoolRegion(school) {
    return SCHOOL_REGION[school] || "US";
  }

  function filteredPrograms() {
    let rows = all.filter((p) => p.region === state.region && p.degreeGroup === state.degree);
    if (state.region === "HK" && state.campus !== "All") {
      rows = rows.filter((p) => p.campusType === state.campus);
    }
    if (state.funding !== "All") rows = rows.filter((p) => p.funding === state.funding);
    if (state.query.trim()) {
      const q = state.query.trim().toLowerCase();
      rows = rows.filter((p) =>
        [
          p.school,
          p.schoolFull,
          p.field,
          p.degree,
          p.notes,
          p.fundingDetail,
          p.location || "",
          p.state || "",
          p.facultyNote || "",
        ]
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

  function facultySchoolsForRegion() {
    const dirs = faculty.directories || {};
    return Object.keys(dirs)
      .filter((school) => schoolRegion(school) === state.region)
      .sort((a, b) => a.localeCompare(b));
  }

  function filteredHighlights(school) {
    let rows = (faculty.highlights || []).filter((f) => schoolRegion(f.school) === state.region);
    if (school) rows = rows.filter((f) => f.school === school);
    if (state.query.trim()) {
      const q = state.query.trim().toLowerCase();
      rows = rows.filter((f) =>
        `${f.school} ${f.name} ${f.title} ${f.areas}`.toLowerCase().includes(q)
      );
    }
    return rows;
  }

  function renderFacultyMode() {
    campusWrap.style.display = "none";
    const schools = facultySchoolsForRegion().filter((school) => {
      if (!state.query.trim()) return true;
      const q = state.query.trim().toLowerCase();
      const d = faculty.directories[school] || {};
      const hitDir = `${school} ${d.note || ""}`.toLowerCase().includes(q);
      const hitPeople = filteredHighlights(school).length > 0;
      return hitDir || hitPeople;
    });

    count.textContent = `教师模式 · ${REGION_LABEL[state.region]} · ${schools.length} 校名录 · 重点导师 ${
      filteredHighlights().length
    } 人（可搜索姓名/方向）`;

    if (!schools.length) {
      list.innerHTML = `<div class="empty">没有匹配学校/老师，请放宽筛选</div>`;
      detail.innerHTML = `<div class="empty">没有匹配结果</div>`;
      return;
    }

    if (!state.selectedFacultyKey || !schools.includes(state.selectedFacultyKey)) {
      state.selectedFacultyKey = schools[0];
    }

    list.innerHTML = schools
      .map((school) => {
        const d = faculty.directories[school] || {};
        const n = filteredHighlights(school).length;
        const selected = school === state.selectedFacultyKey ? "selected" : "";
        const rc = regionClass(state.region);
        return `<article class="card ${rc} ${selected}" data-faculty-school="${school}">
          <div class="card-top">
            <div>
              <h3>${school}</h3>
              <div class="meta">${d.note || "官方教师名录"}</div>
            </div>
            <div class="meta">${n} 位重点</div>
          </div>
          <div class="pills">
            <span class="pill ${rc}">${REGION_LABEL[state.region]}</span>
            <span class="pill">Faculty Directory</span>
            ${n ? `<span class="pill full">重点 AI/CS ${n}</span>` : ""}
          </div>
        </article>`;
      })
      .join("");

    list.querySelectorAll(".card").forEach((el) => {
      el.addEventListener("click", () => {
        state.selectedFacultyKey = el.getAttribute("data-faculty-school");
        render();
      });
    });

    renderFacultyDetail(state.selectedFacultyKey);
  }

  function renderFacultyDetail(school) {
    const d = faculty.directories[school] || {};
    const people = filteredHighlights(school);
    detail.className =
      "panel detail " +
      (state.region === "HK" ? "region-hk" : state.region === "SG" ? "region-sg" : "region-us");

    const peopleHtml = people.length
      ? people
          .map(
            (f) => `<div class="faculty-card">
          <div class="faculty-name">${f.name}</div>
          <div class="meta">${f.title || ""}</div>
          <div class="faculty-areas"><b>研究方向</b>：${f.areas}</div>
          <div class="links" style="margin-top:8px">
            ${f.home ? `<a href="${f.home}" target="_blank" rel="noopener">个人主页</a>` : ""}
            ${f.profile ? `<a href="${f.profile}" target="_blank" rel="noopener" style="opacity:.9">院系简介</a>` : ""}
          </div>
        </div>`
          )
          .join("")
      : `<p class="meta">本站尚未单独摘录该校重点老师；请打开下方官方 Faculty Directory 浏览全员。</p>`;

    detail.innerHTML = `
      <h2>${school} · 老师与研究方向</h2>
      <div class="sub">${d.note || ""}</div>
      <div class="links" style="margin-bottom:12px">
        ${d.all ? `<a href="${d.all}" target="_blank" rel="noopener">全系 Faculty Directory</a>` : ""}
        ${
          d.ai && d.ai !== d.all
            ? `<a href="${d.ai}" target="_blank" rel="noopener" style="opacity:.9">AI / 研究相关名录</a>`
            : d.ai
            ? `<a href="${d.ai}" target="_blank" rel="noopener" style="opacity:.9">AI 相关入口</a>`
            : ""
        }
      </div>
      <section>
        <h4>重点 AI / CS 相关老师（节选）</h4>
        <div class="faculty-list">${peopleHtml}</div>
      </section>
      <p class="meta" style="margin-top:12px">${faculty.disclaimer || ""}</p>
    `;
  }

  function renderProgramList() {
    campusWrap.style.display = state.region === "HK" ? "block" : "none";
    const rows = filteredPrograms();
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
            ${p.facultyDir ? `<span class="pill">有教师名录</span>` : ""}
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

    renderProgramDetail(rows.find((r) => r.id === state.selectedId));
  }

  function renderProgramDetail(p) {
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

    const people = (faculty.highlights || []).filter((f) => f.school === p.school).slice(0, 8);
    const peopleHtml = people.length
      ? `<section><h4>相关重点老师（节选）</h4><div class="faculty-list">${people
          .map(
            (f) => `<div class="faculty-card compact">
          <div class="faculty-name">${f.name}</div>
          <div class="faculty-areas">${f.areas}</div>
          <div class="links" style="margin-top:6px">
            ${f.home ? `<a href="${f.home}" target="_blank" rel="noopener">主页</a>` : ""}
          </div>
        </div>`
          )
          .join("")}</div>
        <p class="meta">更多请切换到「老师主页 / 研究方向」页签，或打开官方 Faculty Directory。</p>
      </section>`
      : "";

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
      ${
        p.facultyDir
          ? `<section>
        <h4>老师 / 研究</h4>
        <p class="meta" style="margin:0 0 8px">${p.facultyNote || ""}</p>
        <div class="links">
          <a href="${p.facultyDir}" target="_blank" rel="noopener">Faculty Directory</a>
          ${
            p.facultyAiDir
              ? `<a href="${p.facultyAiDir}" target="_blank" rel="noopener" style="opacity:.9">AI / Research 入口</a>`
              : ""
          }
        </div>
      </section>`
          : ""
      }
      ${peopleHtml}
      <div class="links">
        <a href="${p.applyUrl}" target="_blank" rel="noopener">注册 / 申请系统</a>
        <a href="${p.infoUrl}" target="_blank" rel="noopener" style="opacity:.9">项目说明页</a>
      </div>
    `;
  }

  function render() {
    if (state.degree === "Faculty") renderFacultyMode();
    else renderProgramList();
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
      state.selectedFacultyKey = null;
      render();
    });
  });

  document.querySelectorAll("#degreeTabs .tab").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.degree = btn.getAttribute("data-degree");
      document.querySelectorAll("#degreeTabs .tab").forEach((b) => {
        b.className = "tab";
        const d = b.getAttribute("data-degree");
        if (d === state.degree) {
          if (d === "PhD") b.classList.add("active-phd");
          else if (d === "Master") b.classList.add("active-master");
          else b.classList.add("active-faculty");
        }
      });
      state.selectedId = null;
      state.selectedFacultyKey = null;
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

  const qInput = $("q");
  if (qInput) qInput.placeholder = "学校 / 老师姓名 / AI / NLP / vision…";

  render();
})();
