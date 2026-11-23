## ProPS-Twin — Implemen

Written for: an ML engineer who is *not* a cyberse

`2026-11-13.`

Method: every claim below cites file:line from th document.

## 0. What this project is (one parag

ProPS-Twin is a *digital twin* (a software simulatio a nuclear power plant. IT = ordinary office/compute systems that run physical plant equipment. Five sim heartbeats, alerts, status records). Scripted cyber s log-only evaluator scores how well a given defens each incident, producing a single scalar reward R.

LLM in a loop that proposes better policies — the m *Prompted Policy Search* (Zhou et al., NeurIPS 20 The repo is deliberately simulation-first: the estate the Python standard library. The cluster, the real m currently empty scaffolding.

## How to read the status labels

Because the *entire estate is synthetic by design*,

## Label

## REAL

## PARTIAL

## DUMMY

## UNKNOWN

A separate flag, synthetic-by-design, marks data accidental stub.

## 1. Summary table

## # Component File

## 1 Seeded RNG helpers research/common/si

`m.py`

## 2 Event model + sink research/common/pr

`ops_log.py`

## 3 IDMZ gateway core services/idmz_gate

`way/core.py`

## 4 Boundary firewall core services/boundary_

`firewall/core.py`

## 5 Eng-station core services/eng_stati

`on/core.py`

## 6 PLC-edge core services/plc_edge/

`core.py`

## 7 Telemetry forwarder core services/telemetry

`_forwarder/core.py`

`docs/IMPLEMENTATION_PLAN.md`

## ntation Plan & Codebase Audit

ecurity domain expert. Security terms are defined on first use. Date:

he code as it exists now. No code was changed to produce this

## graph)

on that stands in for a real system) of the IT/OT security department of er networks; OT = "operational technology", the industrial control mulated components emit security telemetry (a stream of log events — scenarios perturb that stream; a sive policy (a bundle of tunable security settings) detects and contains The eventual research goal (not yet built) is to put an method is ProPS = 025), see docs/props_notes.md.

e, the scenarios and the scoring run today in a bare terminal with only monitoring tool (Wazuh), and the LLM optimizer are later phases and are

"real data" cannot mean "production network traffic". So in this audit:

## Meaning here

Working logic that behaves as the architecture intends. For a *simulator* component this includes synthetic-but-principled telemetry (seeded random noise + deterministic rules).

Real structure, but with placeholder data values, dead wiring (config that is never read, methods never called), or a missing sub-piece.

Stub, empty file, .gitkeep, or an echo-only Makefile target. Not built. Cannot be determined without running something; the exact check is named.

that is intentionally generated (the whole point of a twin) rather than an

## Status Data source Effort to make "real"

`REAL random.Random(seed — (done)`

`) PRNG`

REAL Constructed dicts; — (done)

`SHA-256 ids`

REAL logic / PARTIAL Gaussian noise + M (richer payloads) realism hardcoded attack

`payloads`

REAL logic / PARTIAL Gaussian + hardcoded S–M realism consts REAL logic / PARTIAL Hardcoded signatures M realism (EICAR-TEST,

`CVE-0000-0000)`

REAL logic / PARTIAL Hardcoded checksums S realism REAL Gaussian + buffer-drain — (done)

`state machine`

`ProPS-Twin · page 1`

## # Component File Status

## 8 Scenario controller research/scenario_ REAL

`controller/control`

`ler.py`

## 9 Scenario validator research/scenario_ PARTIAL

controller/models.

`py`

## 10 Scenario catalog research/scenario_ REAL

`controller/catalog`

`.py`

## 11 Evaluation engine research/evaluatio REAL / one PARTIAL

`n/engine.py metric`

## 12 Metric functions research/evaluatio REAL

`n/metrics.py`

## 13 FastAPI wrappers ×5 services/*/main.py PARTIAL

14 estate-config.yaml configs/estate/ PARTIAL (dead config) 15 reward.yaml configs/evaluation PARTIAL (dead config)

`/`

## 16 Policy application path apply_policy() in DUMMY (never called)

`every core`

## 17 Reset path (Step 3.4) controller.py / DUMMY

`Makefile:24`

## 18 Policy Engine research/policy_en DUMMY

`gine/`

## 19 ProPS optimizer + LLM research/props_opt DUMMY

`imizer/`

## 20 Wazuh monitoring wazuh/ DUMMY

## 21 Kubernetes (kind+Calico) k8s/, cluster/ DUMMY

## 22 Docker images services/*/Dockerf PARTIAL / UNKNOWN

ile,

`docker-compose.yml`

`Effort key: S » £1 day, M » 2–4 days, L » 1–3 weeks.`

## 2. Component-by-component audit

## 2.1 research/common/sim.py — seeded randomness — REAL

Two helpers, the only source of stochasticity in the whole simulation. 1 rng_for(seed:int, offset:int=0) -> random.Random — sim.py:7. independent PRNG stream. offset is what keeps component streams plc=3, eng=4, and the *probe* streams use 20/22 so availability probing n (idmz_gateway/core.py:33-34, telemetry_forwarder/core.py:26-27). C offset re-aligns a component to a different noise stream. 1 gauss_nonneg(rng, mean, sigma) -> float — sim.py:12-14. A Gau at 0 (max(0.0, rng.gauss(...))), used for drop-rates, latencies, memory Data source: deterministic PRNG. Reproducible for a fixed seed by desig 2.2 research/common/props_log.py — event model + EventSink — The one JSON object emitted per log line, and the object that stamps it. 1 build_event(...) — props_log.py:31-66. Asserts `severity ˛ {low, me high, critical} (SEVERITIES, line 16), state ˛ {normal, anomalous, faul {enterprise, idmz, supervisory, control, field} (ZONES`, line 18). Ground invariant (see §2.8).

1 deterministic_event_id(experiment_id, component, seq) — props

`docs/IMPLEMENTATION_PLAN.md`

## Data source Effort to make "real"

In-process sim loop — (done)

`Plain validator (Pydantic S`

`promised, not done)`

Built-in dicts + YAML — (done)

Log-only detector over the S (delay fix) event stream Pure functions of counts — (done) No config, frozen clock, M

`shared sink`

Never opened by any .py S (wire it in) Never opened; weights S (wire it in) hardcoded

`n/a M`

`echo stub S`

`2-line README M`

2-line README L (research core)

`.gitkeep only L`

`.gitkeep only L`

`Dockerfiles exist, never M`

`built here`

`Returns an`

from colliding: idmz=0, firewall=1, forwarder=2, never disturbs the telemetry stream Changing seed changes the whole run; changing

ussian clamped

`y %.`

gn.

## — REAL

edium, lt, violation} (STATES, line 17), zone ˛ truth is deliberately not a field — the honesty

`s_log.py:21-27.`

`ProPS-Twin · page 2`

sha256(f"{experiment}|{component}|{seq}")[:32]. This is why a run is byte-reproducible: no random UUIDs.

## 1 EventSink.emit(component, event_type, severity, state, zone, details) —

props_log.py:98-128. Per-component sequence counter (self._seq), optional stdout print (stream), optional in-memory collect (collect). An injected clock callable supplies simulated timestamps. Data source: constructed dicts; timestamps from the controller's virtual clock. REAL.

## 2.3 The five component cores — REAL logic, PARTIAL realism (synthetic-by-design)

All five share the shape: __init__(seed, config) fi reads tunables from config with hardcoded defaults; set_mode(mode) flips behaviour; tick(t, sink) emits events; apply_policy(policy) *exists but is never called* (see §2.9); some have probe(t) for availability.

Important cross-cutting fact: the per-component config dict comes from estate_cfg.get("<component>") in the controller (controller.py:43-47), but every current run passes estate_cfg={} (§2.14), so *in practice every component runs on its built-in defaults* and estate-config.yaml is ignored.

#### (3) IdmzGateway — services/idmz_gateway/core.py — REAL / PARTIAL "IDMZ" = *industrial demilitarized zone*, the buffer network between IT and OT; the gateway brokers traffic crossing it.

`1 Params (core.py:36-42): drop_baseline=0.01, drop_sigma=0.004,`

alert_threshold=3.0, idmz_access_profile="standard", protocol_whitelist=["P1","P2","P3"], probe_sla_ms=50.0. 1 idmz_access_profile ˛ {standard, strict, lockdown} decides containment: _contained = profile ˛ {strict, lockdown} (core.py:59-61). This is the C reward lever for SC-04/SC-06.

1 alert_threshold is **stored and echoed into details.threshold (core.py:70) but never used by the core to decide anything** — detection happens later in the evaluator. This is intentional (DECISIONS.md) but worth knowing: changing it on the component has no effect; the evaluator's copy does. 1 tick() (core.py:64-90) emits by mode: inter_zone_protocol_anomaly (SC-01), idmz_jump_host_crossing (SC-04), unauthenticated_access_attempt (SC-06), else a gateway_heartbeat with a periodic benign near-miss (every 7th tick, _NEAR_MISS_PERIOD=7, +0.12 drop) — bait for false positives. 1 probe(t) (core.py:93-100): latency Gaussian(8,3); lockdown fi ok:False (over-restrictive policy starves legitimate work — the availability cost). 1 handle_request() (core.py:103-119): real whitelist/role/channel logic, but only reachable through the HTTP wrapper (§2.13), which no test or eval uses.

## PARTIAL-realism evidence (hardcoded payloads):

{"protocol": "modbus_unlisted", ...} # core.py:69

`{"src_zone": "enterprise", "dst_zone": "control", "via": "jump-host-01", ...} # core.py:75`

`{"identity": "unknown", "channel": "remote", ...} # core.py:81`

These are fixed strings, not drawn from any model or dataset — fine for a twin, but they are placeholders, not realistic variety.

#### (4) BoundaryFirewall — services/boundary_firewall/core.py — REAL / PARTIAL 1 Params (core.py:30-31): drop_baseline=0.02, boundary_rate_limit=50. 1 packet_storm mode (core.py:45-51) emits two events (packet_storm_volume + boundary_drop_rate) and sets contained = rate_limit <= 60 (_CONTAIN_RATE_LIMIT, line 22). _STORM_PPS=85000 and _STORM_BUMP=0.35 are hardcoded (lines 19-20). #### (5) EngStation — services/eng_station/core.py — REAL / PARTIAL

## 1 Reads access_profile from config key idmz_access_profile (core.py:29) —

i.e. the estate-wide posture governs this host too.

## 1 Modes include privileged_command (SC-03), audit_log_gap (SC-05, omits the

required security_audit_log — the *absence* positive), plus malicious_media, sbom_vuln, hsm_revoked.

## 1 Hardcoded placeholder signatures:

{"device": "usb-1", "signature": "EICAR-TEST"} # core.py:55 (EICAR = standard AV test string) {"package": "libexample", "cve": "CVE-0000-0000"}# core.py:58 (non-existent CVE placeholder) #### (6) PlcEdge — services/plc_edge/core.py — REAL / PARTIAL "PLC" = *programmable logic controller*, the small computer that drives physical I/O; "SIS" = *safety instrumented system*; "WDT" = *watchdog timer*.

1 apply_policy() is an explicit no-op: def apply_policy(self, policy): return (core.py:26-27, comment "no tunable params in v1").

## 1 Emits a wdt_heartbeat every tick plus a firmware-integrity event; modes

firmware_tamper / io_violation / unused_port. Checksums hardcoded ("sha256:baseline" / "sha256:tampered", lines

`21, 39).`

#### (7) TelemetryForwarder — services/telemetry_forwarder/core.py — REAL "Data diode" = a one-way link that lets OT data out to IT but nothing back. 1 Params (core.py:29-33): mem_baseline=0.45, jitter_baseline=2.0, recovery_timeout=60, buffer_drain_ticks=6, probe_sla_ms=50. 1 The most stateful core: leaving a degraded mode owes a bounded buffer-drain (set_mode, core.py:36-40) so recovery is not instantaneous — this is what makes the recovery score Q non-trivial (SC-07). heartbeat_pause emits *nothing* (core.py:58-60) fi the coverage gap. REAL.

## 2.8 research/evaluation/engine.py — the evaluator — REAL (one PARTIAL metric)

The "log-only / fast-mode" scorer. It runs the same detection logic Wazuh would, offline, over the event stream, and never reads ground truth to decide an alert — it matches alerts to ground truth only afterwards, by event_id and time (engine.py:1-18). This ordering is the project's anti-cheating invariant. 1 detect_presence() (engine.py:58-80): an alert fires if drop_rate >= cutoff (threshold path) or state ˛ {anomalous, fault, violation} (state path). cutoff from detection_cutoff(alert_threshold) maps 1..5 fi 0.05..0.25 (engine.py:40-50). 1 detect_coverage_gap() (engine.py:83-98): longest absence of a required periodic signal inside the window; detected if gap ‡ timeout (SC-05/SC-07).

## 1 PARTIAL metric — presence detection delay is hardcoded 0:

matched_delays.extend(0.0 for _ in matched) # engine.py:152 Every presence true-positive contributes delay 0.0 instead of t_alert - t_event. Consequence: metrics.detection_delay_s is always 0 for presence scenarios, and the delay penalty L only becomes non-zero via absence timeouts (engine.py:174) or missed positives. The machinery to measure real delay exists (_t_of) but is not used here.

1 alert_threshold defaults to initial_conditions.alert_threshold or 3.0 (engine.py:116-118); recovery_budget to initial_conditions.recovery_timeout or 60. 1 severity_match is computed and reported (engine.py:226) but **not part of the reward**.

Output doc shape (used by the viz and tests): reward, reward_components {D,C,A,Q,F,L}, metrics, counts {TP,FP,FN,G,B,alerts,probes,probe_ok}, coverage, plus reproducibility metadata (engine.py:211-233).

## 2.9 Policy application path — DUMMY (methods exist, never called)

Every core defines apply_policy(policy) (idmz_gateway/core.py:48, boundary_firewall/core.py:36, eng_station/core.py:34, plc_edge/core.py:26, telemetry_forwarder/core.py:42). A repo-wide search finds no caller of apply_policy anywhere outside the definitions. Policies reach the components *only* through estate_cfg at construction time — and today only scripts/viz_server.py passes a (partial) estate_cfg; the CLI passes {}. The Policy Engine (§2.18) that is meant to call apply_policy does not exist. 2.12 research/evaluation/metrics.py — REAL Pure, unit-tested functions; neutral defaults when a dimension is absent (D=1, C=1, A=1, Q=1). Note SEVERITY_WEIGHT (metrics.py:15) is defined but unused (v1 fp_penalty ignores severity, metrics.py:38-41) — a dead constant reserved for a future extension. DEFAULT_WEIGHTS (lines 17-20) are the weights actually used, because reward.yaml is never loaded

`(§2.15).`

## 2.13 FastAPI wrappers services/*/main.py — PARTIAL

Each exposes /healthz, /state, /control/mode, /tick (idmz adds /request). Problems that make this path non-production:

## 1 Components are built with seed only, no estate config

(idmz_gateway/main.py:19, telemetry_forwarder/main.py:13). 1 /tick always calls tick(0, ...) — the clock is frozen at t=0 (idmz_gateway/main.py:60-61), so every HTTP-emitted event carries the same timestamp; the simulated-time semantics the controller provides are lost.

1 One module-global sink shared across requests, printing to stdout. 1 telemetry_forwarder/main.py:1 docstring says *"FastAPI wrapper for the boundary-protection firewall"* — copy-paste error (harmless, cosmetic). 1 No test or the eval path imports these; they are only exercised by hand via curl / docker-compose.

## 2.14–2.15 Dead config — PARTIAL

1 configs/estate/estate-config.yaml defines per-component tunables and policy defaults, and claims to be "read directly here for local runs" — but a repo-wide search shows no .py file opens it. All CLI runs pass estate_cfg={} (evaluate_local.py:32, demo_local.py:67, make_viz_data.py:43). So the file is documentation, not configuration.

1 configs/evaluation/reward.yaml holds the six reward weights, but evaluate() is always called without a weights= argument (evaluate_local.py:33, make_viz_data.py:44), so DEFAULT_WEIGHTS in metrics.py is always used. The YAML is never read either.

## 2.16 Scenario validator models.py — PARTIAL

Works, but the docstring promises a Pydantic v2 model ("Phase 3 upgrades this", models.py:3-5) that was not done — it remains a hand-rolled validator (validate_scenario, models.py:25-70).

## 2.17–2.22 Not-yet-built phases — DUMMY

## 1 Reset path (Step 3.4): scenarios declare reset_procedure

(catalog.py, e.g. line referencing ["restore_modes", ...]) and models.py:19 lists it as required, but no code executes it; make reset is @echo "[Phase 3] reset scenario via controller API" (Makefile:24). 1 Policy Engine (research/policy_engine/README.md, 2 lines) — DUMMY.

## 1 ProPS optimizer + LLM client (research/props_optimizer/README.md, 2

lines) — DUMMY. *This is the research centrepiece and does not exist yet.*

## 1 Wazuh (wazuh/{rules,decoders,agent-config}/.gitkeep) — DUMMY. Wazuh is an

open-source SIEM (Security Information & Event Management — the tool that reads logs and raises alerts). The log-only evaluator currently *stands in* for it; the "Wazuh-in-the-loop" validation subset is unbuilt.

## 1 Kubernetes (k8s/namespaces/.gitkeep, cluster/.gitkeep) — DUMMY. "kind" =

Kubernetes-in-Docker; "Calico" = a network plugin that enforces zone isolation.

## 1 Docker images: Dockerfiles and docker-compose.yml exist and look

coherent, but no image has been built or run in this environment — UNKNOWN until docker compose build is run.

## 3. Data-flow trace (one run)

`evaluate_local.py`

Entry point: python3 scripts/evaluate_local.py SC-04. 1 evaluate_local.main() fi score("SC-04") (evaluate_local.py:30-33). 2 catalog.load("SC-04") fi scenario dict (YAML if PyYAML present, else built-in

`copy) (catalog.py:150-165).`

1 controller.run_scenario(scenario, estate_cfg={}) (controller.py:50): 2 validate_scenario (models.py:25).

3 build_components(seed, {}) fi five cores on default config (controller.py:41-47) — estate-config.yaml NOT consulted.

## 1 Expand event_sequence {t,duration} fi set/restore schedule

`(controller.py:71-79).`

## 1 Virtual clock loop t=0..end: set_mode at scheduled ticks, then every

component's tick(t, sink) emits events; if the scenario has a probes section, run probes (only SC-07 does)

`(controller.py:84-110).`

1 Build ground-truth rows; optionally persist to SQLite (controller.py:112-132). 2 Return {experiment_id, events, ground_truth}. 3 engine.evaluate(run_result, scenario) (engine.py:112): 4 detect_presence / detect_coverage_gap over telemetry fields only. 5 Match alerts fi ground truth by event_id/time; count TP/FP/FN.

## 6 Compute D,C,A,Q,F,L via metrics.py; reward() with DEFAULT_WEIGHTS

(reward.yaml ignored).

1 Return the result document.

2 _print_human(doc) prints reward + components + counts (evaluate_local.py:36-48). The live backend scripts/viz_server.py wraps the *same* steps 2–4 but streams events over Server-Sent Events and can pass a partial estate_cfg (viz_server.py:53-95).

## 3.1 Flow diagram (dummy / dead parts marked 7)

`flowchart TD`

CLI["evaluate_local.py / demo_local.py / viz_server.py<br/>(entry points)"] --> LOAD["catalog.load(id)<br/>REAL"] LOAD --> RUN["controller.run_scenario<br/>REAL"] ECFG["estate-config.yaml<br/>7 DEAD CONFIG — never read<br/>runs use estate_cfg={}"] -. ignored .-> RUN RUN --> CORES["5 component cores .tick()<br/>REAL logic · synthetic data<br/>payloads hardcoded"] CORES --> SINK["EventSink fi event stream<br/>REAL"] SINK --> EVAL["engine.evaluate<br/>REAL (presence delay=0 7)"] RWD["reward.yaml weights<br/>7 DEAD CONFIG — never read<br/>uses DEFAULT_WEIGHTS"] -. ignored .-> EVAL EVAL --> DOC["result doc: R, D/C/A/Q/F/L, counts<br/>REAL"] AP["core.apply_policy()<br/>7 DUMMY — never called"] -. no caller .-> CORES PE["Policy Engine<br/>7 DUMMY (empty)"] -. should call .-> AP PROPS["ProPS optimizer + LLM<br/>7 DUMMY (empty)"] -. should drive .-> PE PROPS -. reads .-> DOC WZ["Wazuh SIEM<br/>7 DUMMY (empty)"] -. alt detector .-> EVAL K8S["Kubernetes / Wazuh path<br/>7 DUMMY (empty)"] -. deploys .-> CORES HTTP["FastAPI wrappers<br/>PARTIAL (frozen clock, no cfg)"] -. unused by eval .-> CORES RESET["reset path (Step 3.4)<br/>7 DUMMY (echo stub)"] -. should reset .-> RUN Plain-text version of the same flow: entry (CLI/viz) fi load scenario fi run_scenario fi 5 cores.tick() fi EventSink fi evaluate fi result doc (R + components) [dead] estate-config.yaml, reward.yaml : never read [dummy] apply_policy, Policy Engine, ProPS/LLM, Wazuh, k8s, reset path [partial] FastAPI wrappers, presence delay=0, scenario validator

## 4. Implementation plan (turn each DUMMY/PARTIAL real)

Tasks are ordered so dependencies come first. Each gives: what to build, files touched, the real source/model that replaces the stub, new config, and a check.

## Tier A — finish the simulation core (low effort, unblock everything)

T1 — Wire estate-config.yaml and reward.yaml into the run/eval path

`*(fixes #14, #15; effort S)*`

## 1 Build: a small loader that reads configs/estate/estate-config.yaml and passes

it as estate_cfg to run_scenario; read configs/evaluation/reward.yaml and pass weights= to evaluate. 1 Files: new research/common/config.py; edit scripts/evaluate_local.py:32, scripts/demo_local.py:67, scripts/make_viz_data.py:43, scripts/viz_server.py:89-95. 1 Config: none new; just stop ignoring the two existing files. 1 Check: change w_c in reward.yaml and confirm SC-04's R changes; set idmz_access_profile: strict in estate-config.yaml and confirm SC-04 C goes 0fi1 from the CLI (today only the viz backend can do that).

1 Depends on: none. Do this first — it makes config real for every later task. T2 — Implement the reset path (Step 3.4) *(fixes #17; effort S)*

## 1 Build: a reset_scenario() in the controller that executes each step in

reset_procedure (restore_modes, restore_policy_baseline, flush_state, new_experiment_id); wire make reset. 1 Files: research/scenario_controller/controller.py; Makefile:24. 1 Check: a pytest that runs a scenario, resets, re-runs, and asserts identical event_ids and a fresh experiment_id counter.

1 Depends on: none.

T3 — Measure real presence detection delay *(fixes #11 PARTIAL; effort S)*

## 1 Build: replace matched_delays.extend(0.0 ...) (engine.py:152) with

t_alert - t_event per matched alert (both available via _t_of). 1 Files: research/evaluation/engine.py.

1 Check: a unit test where an alert fires 3 ticks after the event asserts metrics.detection_delay_s == 3.0 and that L rises accordingly; confirm the SC-01..SC-07 suite rewards shift only where expected.

1 Depends on: none (but re-baseline the viz demo data after, make viz-data). T4 — Upgrade the scenario validator to Pydantic v2 *(fixes #16; effort S)*

## 1 Files: research/scenario_controller/models.py; add pydantic (already in

requirements.txt).

## 1 Check: existing tests/scenarios/test_scenario_catalog.py stays green; add a

test that a malformed scenario raises a ValidationError. 1 Depends on: none.

T5 — Broaden availability probing & payload realism *(fixes #3–6 PARTIAL; effort S–M)*

## 1 Build: add probes sections to the scenarios where availability matters (today

only SC-07 has one, catalog.py:145); optionally parameterise the hardcoded attack payloads (protocols, CVEs, checksums) from small lookup tables or a seeded generator so runs show variety. 1 Files: configs/scenarios/*.yaml, catalog.py, the cores. 1 Check: SC-04/SC-06 report probes > 0 and a meaningful A; make test green.

## Tier B — the policy loop (the research core)

`T6 — Policy Engine *(fixes #16, #18; effort M)*`

## 1 Build: a module that (a) validates a candidate policy against bounds/safety

constraints (H5 in docs/protocol.md) and (b) applies it by calling each core's apply_policy() (today never called, §2.9) — or by constructing estate_cfg and re-running.

1 Define "policy" concretely: `{alert_threshold:int 1..5, idmz_access_profile:enum, boundary_rate_limit:int, recovery_timeout:int, protocol_whitelist:subset}`. 1 Files: research/policy_engine/ (new engine.py, schema.py). 1 Config: configs/policies/*.yaml (dir exists, empty). 1 Check: apply strict fi SC-04 C=1; apply an out-of-bounds policy fi rejected; a round-trip test that an applied policy changes the reward deterministically.

T7 — ProPS optimizer + LLM client *(fixes #19; effort L — the centrepiece)*

## 1 Build: (a) an LLM client abstraction (provider-agnostic; start with a

local/mock backend so the loop is testable offline), (b) a prompt template that serializes the current best policies + rewards and asks for the next candidate, (c) the closed-loop search that proposes fi validates (T6) fi evaluates (§2.8) fi scores fi feeds back. Compare against random search and TPE (Tree-structured Parzen Estimator, a standard Bayesian-optimization baseline) per hypotheses H1–H4. 1 Files: research/props_optimizer/ (new llm.py, prompt.py, search.py).

## 1 Config: budget B, seeds, repetitions (pre-register in

docs/protocol.md before any run), model id/endpoint via env. 1 Check: on a fixed mock LLM, the loop improves mean reward over a random-search baseline for the same budget on held-out seeds; H5 (no accepted policy violates a hard constraint) asserted every iteration.

## 1 Depends on: T1, T3, T6. Define docs/props_notes.md adaptations first (the

table at props_notes.md is half-empty).

## Tier C — the real monitoring stack (validation realism)

T8 — Docker images build & verify *(fixes #22; effort M)* 1 Build: confirm the five images build and the HTTP wrappers work; fix the wrapper issues in §2.13 (inject estate config; use a real per-run clock/sink; fix the telemetry_forwarder/main.py docstring).

1 Files: services/*/main.py, services/*/Dockerfile, docker-compose.yml. 1 Check: docker compose up; curl :8001/healthz ok; drive a mode change and see timestamped events with distinct event_ids (not all t=0).

T9 — Kubernetes (kind + Calico), Phase 1 *(fixes #21; effort L)*

## 1 Build: a kind cluster, namespaces per zone, Calico NetworkPolicies enforcing

zone isolation, manifests to deploy the five images. Fill docs/VERSIONS.md (currently an empty table).

## 1 Files: cluster/, k8s/namespaces/, new k8s/*.yaml; Makefile cluster

targets (today echo stubs, Makefile:19-24).

## 1 Check: make cluster && make deploy; pods Running; a cross-zone request

blocked by policy.

T10 — Wazuh-in-the-loop, Phase 4 *(fixes #20; effort L)*

## 1 Build: Wazuh decoders + rules that reproduce the log-only detector's decisions

on real log ingestion; a verifier for the 5-stage logfialert chain; wire a "Wazuh-in-the-loop" evaluation subset that cross-checks the fast-mode evaluator.

1 Files: wazuh/{decoders,rules,agent-config}/; a verify path; Makefile:21.

## 1 New config: Wazuh rule ids « event_type families (mapping in

docs/signals.md).

## 1 Check: for the validation subset, Wazuh alerts match the fast-mode evaluator's

TP/FP within a stated tolerance (reach milestone-1).

## Tier D — analysis

T11 — Reward-weight sensitivity analysis, Phase 7 *(effort M)* 1 Build: sweep the reward.yaml weights (now live after T1) and report how the ProPS ranking of policies moves — a threat-to-validity named in docs/protocol.md.

`1 Depends on: T1, T6, T7.`

## Suggested order

T1 fi {T2, T3, T4, T5} (finish the core; all small, parallelizable) T1 fi T6 fi T7 (policy loop; the research deliverable) T1 fi T8 fi T9 fi T10 (real stack; validation realism)

`{T1,T6,T7} fi T11 (sensitivity)`

T1 unblocks everything. The research result (H1–H4) needs only Tier A + Tier B — the cluster and Wazuh (Tier C) add *validation realism* but are not on the critical path to a first optimization result.

## 5. Open questions / UNKNOWN

## 1 Docker build (#22): not attempted in this environment; run

docker compose build to confirm the images compile and the wrappers import research.* correctly inside the container (the Dockerfiles must copy the repo root, not just services/).

## 1 PyYAML parity: catalog.load() prefers YAML and falls back to built-in

dicts; a test asserts they match *only when PyYAML is importable* (catalog.py:9-13). Confirm the venv has PyYAML so the canonical YAML — not the in-code copy — is what actually runs. Run: python3 -c "import yaml; print(yaml.__version__)".

1 Which LLM/provider for T7 is a project decision, not inferable from code.
