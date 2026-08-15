# AGENTS.md

These instructions apply to the whole of `thoth-pub/thoth-client`.

They are a repository-local specialization of Thoth's shared engineering-control
doctrine. They do not restate that doctrine in full; read the canonical shared
documents (section 2) together with this file.

## 1. Repository identity

This repository is the **standalone Python client** for Thoth's APIs. It is
published to PyPI as the distribution:

```text
thothlibrary
```

Verified from `setup.py` (`name="thothlibrary"`, "Python client for Thoth's
APIs") and `thothlibrary/__init__.py`, which exports `ThothClient`,
`ThothQuery`, `ThothMutation`, `ThothRESTClient` and `ThothError`.

This repository is **not** the internal Rust `thoth-client` workspace member
located inside `thoth-pub/thoth` at `thoth-client/`. That crate is a Cargo
workspace member depended on only by `thoth-export-server` within the same
workspace, is not published independently, and shares nothing with this
repository beyond the name and the API it targets.

Do not conflate the two. Specifically:

- a task authorized against the Rust `thoth-client` crate in `thoth-pub/thoth`
  does **not** authorize any change here, and the reverse is equally true;
- "thoth-client" in a specification, issue or review comment is ambiguous;
  resolve it to either `thoth-pub/thoth-client` (this repository, Python) or
  `thoth-pub/thoth` `thoth-client/` (internal, Rust) before acting;
- do not import doctrine, build commands, test commands or release procedure
  from the Rust workspace into this repository.

## 2. Shared doctrine and authority

Canonical shared doctrine is maintained in `thoth-pub/thoth`:

- `AGENTS.md` (root);
- `docs/engineering/AGENTS.md`;
- `docs/engineering/ai-delivery/operating-model.md`;
- `docs/engineering/ai-delivery/implementation-handoff-template.md`;
- `docs/engineering/repository-map/contracts.md`;
- `docs/engineering/repository-map/repositories/thoth-client.md`.

This repository has no `docs/engineering/` tree of its own. Do not assume one
exists here, and do not create one without separate authorization.

The following apply to every task in this repository:

- **the owning GitHub issue (and its linked pull request) is the live task
  ledger.** It carries the current gate, approved specification reference,
  risk, exact authorized base, active branch/PR, blockers and next action. A
  task must be resumable from that durable evidence alone, without prior
  conversation history;
- **the exact task authorization controls implementation.** Where a prompt,
  conversation or memory conflicts with the approved specification or with
  live repository evidence, the prompt loses;
- **actions are deny-by-default.** Any action not explicitly authorized for the
  task is denied;
- **permissions are granular and non-transitive.** Source-write does not imply
  commit; commit does not imply push; push does not imply pull-request
  mutation; repository-write does not imply issue/comment mutation;
  merge does not imply deployment; deployment does not imply production
  activation; API/provider read does not imply API/provider write;
- **an implementing agent cannot approve its own work.** Independent review is
  performed by a different agent instance or person.

Where live repository evidence contradicts any document — including this one —
stop and reconcile against the live evidence rather than resolving it
unilaterally.

## 3. Branch topology

Verified current topology of this repository:

```text
development:      develop
default/release:  master
```

Normal work:

```text
develop -> feature/<area>/<task-id> -> develop
```

Release integration is `develop -> master`.

This repository currently conforms to the shared `develop -> master` topology.
Do not normalize, rename or otherwise alter branch topology under an ordinary
implementation task. Verify the actual base branch and its exact head before
branching; never assume it.

## 4. Mandatory task identity

Before any substantive work, record and verify:

```text
Programme / stage:
Owning GitHub issue:
Task ID:
Approved specification:
Risk: LOW | MEDIUM | HIGH | CRITICAL
Exact authorized base SHA (40 characters):
Task branch:
PR target:
Dependencies:
Authorized write budget (existing files):
Authorized new-file paths:
Prohibited paths:
Action-authorization matrix:
Cross-repository impact:
Tests / validation:
Package / public API effects:
Release / publication effects:
HOLD / STOP conditions:
```

If any item is unknown, treat it as missing work rather than filling it by
inference. If the base branch has moved from the exact authorized SHA, stop and
return `HOLD - AUTHORIZED BASE MOVED` with the authorized SHA, the current SHA,
the intervening commits and whether they appear relevant. Do not silently
rebase the authorization onto a new head.

Inspect every file in the write budget before editing it.

## 5. GraphQL boundary

Verified implementation:

- `thothlibrary/client.py` provides `ThothClient`;
- the default Thoth API endpoint is `https://api.thoth.pub`
  (`THOTH_ENDPOINT` in `thothlibrary/client.py`);
- GraphQL requests are sent to the `/graphql` path derived from that endpoint;
- the client supports Thoth schema version `1.0.0` (`THOTH_VERSION`);
  constructing `ThothClient` with any other version raises `ValueError`;
- `thothlibrary/graphql.py` (`GraphQLClientRequests`) is the HTTP transport;
- `thothlibrary/query.py` and `thothlibrary/mutation.py` build queries and
  mutations; `thothlibrary/thoth-1_0_0/` holds the version-specific endpoints,
  queries and response structures;
- authentication injects a bearer personal access token
  (`ThothClient.set_token`/`login` -> `GraphQLClient.inject_token`, sent as the
  `Authorization` header).

**This GraphQL surface is not read-only.** `ThothClient` exposes create, update,
delete, move and file-upload mutation methods across the Thoth domain
(publishers, imprints, works, publications, contributions, locations and more),
in addition to queries and counts.

Therefore:

- running client mutations against a live Thoth API is an **external write** and
  requires explicit, separate authorization naming the target environment;
- authorization to modify source in this repository, or to run local
  validation, never implies authorization to execute a mutation against any
  live API;
- use of a **production** personal access token is never implied by
  source-write or validation authorization, and requires its own explicit
  authorization;
- API read authorization does not extend to API write authorization.

## 6. REST / export boundary

This repository also ships a REST client for Thoth's export API:

- `thothlibrary/rest.py` provides `ThothRESTClient`, defaulting to the endpoint
  `https://export.thoth.pub`;
- `thothlibrary/rest_cli.py` exposes it on the command line;
- `thothlibrary/rest_structures.py` builds the returned object structures;
- the surface covers format, specification and platform discovery
  (`/formats/`, `/specifications/`, `/platforms/` and their per-identifier
  routes) and work/publisher export routes
  (`/specifications/{id}/work/{work_id}`,
  `/specifications/{id}/publisher/{publisher_id}`).

An upstream change to any of the following may require a compatibility change
here:

- Thoth GraphQL schema or semantics;
- REST/export routes;
- export format, specification or platform identifiers;
- response structures consumed by `rest_structures.py` or
  `thothlibrary/thoth-1_0_0/structures.py`;
- authentication assumptions (for example PAT header semantics, or a route
  becoming authenticated).

Do not scope such an upstream change as single-repository work without first
inspecting this repository. Equally, do not assume every export-format change
is breaking here: assess the specific change against what `ThothRESTClient`,
`rest_structures.py` and the versioned structures actually consume, and record
the conclusion.

## 7. Cross-repository compatibility

`thoth-pub/thoth` owns the canonical domain, the GraphQL API and the
REST/export API and formats. This repository **consumes** those contracts; it
does not own them.

For a breaking GraphQL or REST/export change:

1. inspect this repository before approving upstream scope, and record whether
   it requires a change or remains compatible and why;
2. define the concrete compatibility requirement for this client;
3. use a repository-local bounded task, branch and pull request here — no
   single agent gets unrestricted write access to both repositories for the
   same task;
4. do not let this repository guess an unmerged upstream contract; wait for the
   upstream change to merge, or consume an explicitly pinned preview;
5. define the merge and release compatibility order across the affected
   repositories.

External users of the published `thothlibrary` package are **not fully
enumerable** from Thoth's repositories. Known first-party consumers are
therefore not a sufficient impact analysis: public package compatibility must
be assessed independently, and a breaking GraphQL or REST/export change should
be treated as public-API-breaking by default.

## 8. Public Python package and API

Changes to any of the following may be public API changes:

- exported classes and module-level names (`thothlibrary/__init__.py`
  `__all__`);
- method names, arguments, argument order, defaults or removal;
- returned structures and their field names;
- the set of supported Thoth GraphQL schema versions;
- REST client routes, structures and defaults;
- declared dependencies and supported Python versions.

A task touching any of these must explicitly consider:

- backwards compatibility, including deprecation path where removal is
  proposed;
- semantic/package versioning (`__version__` in `thothlibrary/__init__.py`,
  consumed by `setup.py`);
- migration guidance for external consumers where required;
- compatibility with the relevant Thoth API version;
- whether a release is needed, and if so under separate authorization
  (section 12).

None of the above may be changed under `CTRL-REPO-CLIENT-01`, which is
documentation-only.

## 9. Safe validation

Use this repository's actual test path. Do not invent lint, type-check,
coverage or build gates it does not have.

Dependency installation, where required:

```bash
python -m pip install -r requirements.txt
```

Unit tests, matching what CI runs:

```bash
python -m unittest thothlibrary.tests.test_rest thothlibrary.thoth-1_0_0.tests.tests
```

For a documentation-only change, also run:

```bash
git diff --check
```

Note that `thothlibrary/tests/test_queries.py` exists in the tree but is not
part of the CI command above. State accurately which modules were run; do not
claim broader coverage than was executed.

Do not invoke `ThothClient` or `ThothRESTClient` against production APIs as a
smoke test, and do not use a production personal access token. Tests must not
be pointed at production.

Record the exact commands and their concise results. "Tests passed" is not an
acceptable report.

## 10. Build artefacts

Do **not** run:

```text
python setup.py sdist bdist_wheel
```

for a documentation-only or `AGENTS.md`-only task. It creates package artefacts
and directories (`dist/`, `build/`, `*.egg-info/`) outside such a task's
authorized write budget, and proves nothing about a Markdown change.

Package builds may be appropriate in a future package-change task, provided
that task explicitly accounts for the artefacts produced and their cleanup.

## 11. Continuous integration

`.github/workflows/tests.yml` (verified):

- triggers on every `pull_request`, and on pushes to `master` and `develop`;
- runs on `ubuntu-latest` with Python `3.11`;
- installs `requirements.txt`;
- runs `python -m unittest thothlibrary.tests.test_rest thothlibrary.thoth-1_0_0.tests.tests`.

Opening or updating a pull request therefore triggers this workflow
automatically; that is an expected side effect of authorized PR actions.

This workflow does **not** prove compatibility against arbitrary live Thoth API
versions. It runs local unit tests only. Do not present a green CI run as
evidence of live API compatibility.

Manual CI dispatch or rerun is a distinct action and is denied unless
explicitly authorized.

## 12. Release and PyPI publication

`.github/workflows/publish-to-pypi.yml` (verified):

```yaml
on:
  release:
    types: [published]
```

It builds source and wheel distributions from `setup.py` and publishes with
`pypa/gh-action-pypi-publish` under `permissions: id-token: write` (trusted
publishing via OIDC).

Consequences:

- **publishing a GitHub release is also a PyPI publication action.** There is
  no separate "just tag it" step that avoids publishing;
- release, tag and publication must always be authorized separately and
  explicitly, naming the version;
- creating or updating an ordinary pull request is **not** release
  authorization, and merging a pull request is not release authorization;
- an approved independent review authorizes nothing beyond the review decision.

Opening a pull request must not trigger this workflow, because it requires a
published GitHub release. If a publication, provider or other unexpected
external effect nevertheless occurs, report it immediately, do not interact
with it manually, and do not rerun or attempt to compensate for it without
separate authorization.

## 13. Secrets and external effects

Production credentials are not required for ordinary local unit tests.

No personal access token, API key or other credential may be added to:

- source;
- this file;
- test fixtures;
- logs or reported output;
- committed configuration.

Provide credentials, when a task is explicitly authorized to use them, through
the environment (for example the `THOTH_PAT` variable the CLI reads) and never
by committing them.

API/provider reads and writes are distinct permissions. A future task
authorized to perform an unauthenticated export **read** is not thereby
authorized to run GraphQL **mutations**, and no API authorization implies
release or publication authorization.

Do not log tokens, secrets, raw credentials or unbounded upstream response
bodies.

## 14. Independent review and completion

Independent source review binds to an **exact head SHA**. Any later commit on
the branch, substantive or not, invalidates the previous approval and requires
fresh review at the new head.

Do not create a commit whose only purpose is copying a review, approval or
merge identifier into a repository file: that moves the head and invalidates
the review it records. Pull-request body edits and GitHub comments do not move
the head and may carry such evidence.

An `APPROVED` review authorizes nothing beyond the review decision. It does not
authorize:

- merge;
- a GitHub tag or release;
- PyPI publication;
- deployment;
- production activation.

Each of those is a separate action requiring its own explicit authorization.

## 15. Stop conditions

Stop and return `HOLD`/`BLOCKED` rather than improvising when:

- the base branch has moved from the exact authorized SHA before branch
  creation;
- an authorized new file unexpectedly already exists;
- the owning issue has materially changed;
- a path outside the authorized write budget appears necessary;
- package, public API or workflow code would have to change under a task that
  does not authorize it;
- a release, version bump or publication action becomes necessary;
- production credentials or live API mutations would be required;
- a public-contract fact cannot be verified from live evidence;
- unrelated working-tree changes cannot be isolated safely;
- authoritative sources conflict.

Never broaden the write budget or action authorization yourself, and never
merge or approve your own work.
