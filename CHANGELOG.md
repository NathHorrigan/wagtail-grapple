## Unreleased

## [0.28.0] - 2025-02-18

### Added

-   Support for Wagtail 6.3 and 6.4 and Python 3.13 ([#416](https://github.com/torchbox/wagtail-grapple/pull/416)) @mgax
-   Support for [`ImageBlock`](https://docs.wagtail.org/en/stable/releases/6.3.html#imageblock-with-alt-text-support) ([#419](https://github.com/torchbox/wagtail-grapple/pull/419)) @mgax

### Removed

-   Support for Wagtail < 6.3 and Python 3.8 ([#416](https://github.com/torchbox/wagtail-grapple/pull/416)) @mgax

## [0.27.0] - 2024-09-24

### Added

-   Add an `in_menu` filter ([#402](https://github.com/torchbox/wagtail-grapple/pull/402)) @dopry
-   Add ability to speficy the search operator ([#406](https://github.com/torchbox/wagtail-grapple/pull/406)) @dopry

### Changed

-   `SnippetObjectType` is replaced with `SnippetInterface` ([#405](https://github.com/torchbox/wagtail-grapple/pull/405)) @mgax

### Fixed

-   `value` not being queryable on `EmbedBlock` ([#399](https://github.com/torchbox/wagtail-grapple/pull/399))@JakubMastalerz
-   Circular import when defining custom `PageInterface` ([#404](https://github.com/torchbox/wagtail-grapple/pull/404)) @mgax

## [0.26.0] - 2024-06-26

### Changed

-   Make value fields nullable on `PageChooserBlock`, `SnippetChooserBlock`, `DocumentChooserBlock` and `ImageChooserBlock` ([#396](https://github.com/torchbox/wagtail-grapple/pull/396))

## [0.25.1] - 2024-04-21

### Changed

-   Remove pre-Wagtail 5.2 conditional code
-   Ensure renditions with `preserveSVG` return the original if no valid filters are passed ([#390](https://github.com/torchbox/wagtail-grapple/pull/390))

## [0.25.0] - 2024-04-12

### Changed

-   Add support for Wagtail 6, Django 5 ([#387](https://github.com/torchbox/wagtail-grapple/pull/387)) @Morsey187

### Removed

-   Support for Django < 4.2, Wagtail < 5.2

## [0.24.0] - 2024-01-05

### Changed

-   Renamed `RedirectType` to `RedirectObjectType` ([#380](https://github.com/torchbox/wagtail-grapple/pull/380)) @JakubMastalerz
-   `RedirectsQuery` now returns a `Redirect` for each associated `Site` ([#380](https://github.com/torchbox/wagtail-grapple/pull/380)) @JakubMastalerz
    -   Added `site` field on `RedirectObjectType`
    -   Changed `new_url` field on `RedirectObjectType` to be optional

### Fixed

-   `test_src_set_invalid_format` not working with Wagtail 5.2 and above. ([#378](https://github.com/torchbox/wagtail-grapple/pull/378)) @JakubMastalerz

## [0.23.0] - 2023-09-29

### Added

-   Implement `preserveSvg` flag for `srcSet` ([#370](https://github.com/torchbox/wagtail-grapple/pull/370)) @mgax

### Changed

-   `preserveSVG` is true by default ([#371](https://github.com/torchbox/wagtail-grapple/pull/371)) @mgax
-   Improvements to the CI pipelines

## [0.22.0] - 2023-09-18

### Added

-   Add global mechanism for overriding the base `PageInterface` ([#325](https://github.com/torchbox/wagtail-grapple/pull/325)) @Leden, @dopry, @zerolab
-   Allow defining additional interfaces via `graphql_interfaces` ([#366](https://github.com/torchbox/wagtail-grapple/pull/366)) @mgax, @zerolab
    This applies to all models, including StreamField blocks

## [0.21.0] - 2023-09-04

### Added

-   Support for SVGs when using Wagtail 5.0+ ([#359](https://github.com/torchbox/wagtail-grapple/pull/359)) @zerolab
    You can differentiate images using the `isSVG` property. The image rendition field accepts a `preserveSvg` argument
    which will help prevent raster image operations (e.g. format-webp, bgcolor, etc.) being applied to SVGs. [Reference](https://docs.wagtail.org/en/stable/topics/images.html#svg-images)

### Changed

-   Use consistent ID type for pages and page queries ([#350](https://github.com/torchbox/wagtail-grapple/pull/350)) @estyxx
    ⚠️ Warning note: if your query looked like `query($id: Int) { page(id: $id) { ... } }`, it must now be `query($id: ID) { page(id: $id) { ... } }`
-   Pass the `GraphQLResolveInfo` object to the StreamField callables ([#356](https://github.com/torchbox/wagtail-grapple/pull/356)) @zerolab
    This is passed as the `info` kwarg.
-   The image rendition query will now surface any errors when:
-   using filters not present in the `ALLOWED_IMAGE_FILTERS` Grapple setting,
-   there are no filters to apply (for example you are requesting an SVG rendition but supply raster image operations)
-   the source image is not present

## [0.20.0] - 2023-07-10

### Added

-   `searchScore` field for pages ([#320](https://github.com/torchbox/wagtail-grapple/pull/320)) @dopry
-   Support for passing callables for resolving `StreamField` block values ([#322](https://github.com/torchbox/wagtail-grapple/pull/322)) @bbliem, @dopry
-   Support for graphene type arguments, chiefly `description` and `deprecation_reason ([#333](https://github.com/torchbox/wagtail-grapple/pull/333)) @Morsey187, @jams2
-   Testing with PostgreSQL ([#301](https://github.com/torchbox/wagtail-grapple/pull/301)) @dopry

### Changed

-   All middleware defined in the decorator will be used ([#281](https://github.com/torchbox/wagtail-grapple/pull/281)) @seb-b
-   `GraphQLError` no longer raised when querying for a site by hostname that doesn't match any `Site`s (`None` is returned instead) - ([#342](https://github.com/torchbox/wagtail-grapple/pull/342)) @kbayliss
-   When querying pages with a site filter (e.g. `pages(site: "localhost")`) whose hostname does not match a `Site`, we no longer return pages for the first `Site` (`None` is returned instead) - ([#342](https://github.com/torchbox/wagtail-grapple/pull/342)) @kbayliss
-   When querying site setting/settings without a site filter (e.g. `setting(name: "SocialMediaSettings")`) and there are multiple `Site`s, we no longer return settings for the first `Site` (`GraphQLError` is raised instead) - ([#342](https://github.com/torchbox/wagtail-grapple/pull/342)) @kbayliss
-   Updated to graphiql 2.4.x
-   Switched to using [Ruff](https://beta.ruff.rs/docs/) for linting ([#334](https://github.com/torchbox/wagtail-grapple/pull/334)) @zerolab
-   Switched to using [flit](https://flit.pypa.io/en/latest/) for building the package ([#335](https://github.com/torchbox/wagtail-grapple/pull/335)) @zerolab
-   Switched to PyPI Trusted Publishing. @zerolab

### Fixed

-   Fix rendition interface definition ([#337](https://github.com/torchbox/wagtail-grapple/pull/337)) @engAmirEng, @zerolab

### Removed

-   Channels support ([#336](https://github.com/torchbox/wagtail-grapple/pull/336)) @zerolab
-   Unused preview template, and Gatsby reference
-   Support for Wagtail < 4.1

## [0.19.2] - 2023-01-17

### Fixed

-   Fix order_by_relevance needed for Postgres and queryset ordered searches ([#299](https://github.com/torchbox/wagtail-grapple/pull/299)) @dopry

## [0.19.1] - 2023-01-09

### Fixed

-   An error when using deprecated settings. ([#298](https://github.com/torchbox/wagtail-grapple/pull/298)) Thanks @kbayliss for the heads up
-   Previews for drafts ([#277](https://github.com/torchbox/wagtail-grapple/pull/277)) @dopry

## [0.19.0] - 2023-01-09

### Changed

-   Upgrade graphene to v3 ([#143](https://github.com/torchbox/wagtail-grapple/pull/143), [#285](https://github.com/torchbox/wagtail-grapple/pull/285)) @fabienheureux, @dopry
-   Change search queries to respect specified order ([#292](https://github.com/torchbox/wagtail-grapple/pull/292)) @dopry
-   Allows installation on Django 4.1

## [0.18.1] - 2022-11-29

### Changed

-   Upgrade graphiql to 2.0.13, React to 18.2.0 ([#273](https://github.com/torchbox/wagtail-grapple/pull/273)) @dopry

## [0.18.0] - 2022-10-31

### Added

-   New `GraphQLRichText` field type, and RichText(Scalar) type ([#266](https://github.com/torchbox/wagtail-grapple/pull/266)) @jams2

### Fixed

-   Fix errors with attributes when checking for rich text fields ([#261](https://github.com/torchbox/wagtail-grapple/pull/261)) @Tijani-Dia
-   Fix IDs for `StrucBlock`s nested in `StreamBlock`s ([#269](https://github.com/torchbox/wagtail-grapple/pull/269)) @Tijani-Dia
-   Renditions are prefetched when using Wagtail 3.0+ ([#271](https://github.com/torchbox/wagtail-grapple/pull/269)) @zerolab with hat-tip to @Tijani-Dia

## [0.17.1] - 2022-08-24

### Fixed

-   Fix errors with attributes when checking for rich text fields ([#261](https://github.com/torchbox/wagtail-grapple/pull/261)) @Tijani-Dia

## [0.17.0] - 2022-08-19

### Added

-   Multi-site page query filters. ([#258](https://github.com/torchbox/wagtail-grapple/pull/258)) @kaedroho
-   Ancestor, parent filter for the pages query. ([#240](https://github.com/torchbox/wagtail-grapple/pull/240)) dopry
-   Proper snippet values in `SnippetChooserBlock`. ([#256](https://github.com/torchbox/wagtail-grapple/pull/256)) @jams2
-   Support specifying format in image srcSet query. ([#257](https://github.com/torchbox/wagtail-grapple/pull/257)) @jams2
-   `RICHTEXT_FORMAT` setting for the rich text field. ([#259](https://github.com/torchbox/wagtail-grapple/pull/259)) @zerolab
    Note: both now use the "html", rendered format. Set it to "raw" for the database representation.
-   Support for comma separated list of `content_type`s in the `pages` query. ([#250](https://github.com/torchbox/wagtail-grapple/pull/250)) @dopry

### Changed

-   Removed unnecessary processing of embed urls. ([#252](https://github.com/torchbox/wagtail-grapple/pull/252)) @dopry
-   Update graphiql version to fix XSS vulnerability. ([#248](https://github.com/torchbox/wagtail-grapple/pull/248)) @dopry
-   `RichTextField` and `RichTextBlock` output now uses the `RICHTEXT_FORMAT` setting for consistent output. ([#259](https://github.com/torchbox/wagtail-grapple/pull/259)) @zerolab, @Tijani-Dia
    Note: `RichTextBlock`'s `rawValue` output is always the non-rendered version. h/t @isolationism

## [0.16.0] - 2022-08-03

### Added

-   Support for Generic Settings models ([#233](https://github.com/torchbox/wagtail-grapple/pull/233)) Thanks @kaedroho
-   Support for Wagtail 4.0 ([#232](https://github.com/torchbox/wagtail-grapple/pull/232)) Thanks @kaedroho

### Fixed

-   [wagtailmedia](https://github.org/torchbox/wagtailmedia/) import error when package installed,
    but not used in `INSTALLED_APPS` ([#235](https://github.com/torchbox/wagtail-grapple/pull/235)) Thanks @kaedroho

### Removed

-   All blind `except:` clauses ([#236](https://github.com/torchbox/wagtail-grapple/pull/236)) Thanks @kaedroho

## [0.15.1] - 2022-06-23

### Added

-   Add missing `urlPath` to page field under `SiteObjectType` ([#230](https://github.com/torchbox/wagtail-grapple/pull/230)) Thanks @Morsey187

## [0.15.0] - 2022-06-07

### Added

-   Support for Wagtail 3.0 ([#229](https://github.com/torchbox/wagtail-grapple/pull/229)) @fabienheureux
-   Additional linting to improve consistency between contributors ([#223](https://github.com/torchbox/wagtail-grapple/pull/223)) @kbayliss

### Fixed

-   Check callable field sources before execution ([#228](https://github.com/torchbox/wagtail-grapple/pull/228)) Thanks @danbentley

### Removed

-   Support for Wagtail < 2.15 ([#229](https://github.com/torchbox/wagtail-grapple/pull/229)) @fabienheureux

## [0.14.1] - 2022-03-31

### Changed

-   StreamField block values are passed to callables ([#222](https://github.com/torchbox/wagtail-grapple/pull/222)). Thanks @kbayliss
-   README and linting tidy up. Thanks @kbayliss

## [0.14.0] - 2022-03-25

### Added

-   Support for attributes and callable sources within `StreamField`s ([#220](https://github.com/torchbox/wagtail-grapple/pull/220)). Thanks @kbayliss
-   flake8/isort linting configuration

## [0.13.0] - 2022-02-25

### Added

-   Support for Wagtail 2.16 ([#212](https://github.com/torchbox/wagtail-grapple/pull/212)). Thanks @fabienheureux
-   Support for queryset slicing when using `searchQuery` ([#206](https://github.com/torchbox/wagtail-grapple/pull/206)). Thanks @protasove
-   Tweak for GitHub to show dependents ([#216](https://github.com/torchbox/wagtail-grapple/pull/216)). Thanks @thibaudcolas
-   Switched to the latest stable release of [black](https://github.com/psf/black)

### Removed

-   Deprecated use of `ugettext_lazy` [#202](https://github.com/torchbox/wagtail-grapple/pull/202). Thanks @13hakta
-   Support for Wagtail < 2.14, Python < 3.7

### Fixed

-   Docker build ([#210](https://github.com/torchbox/wagtail-grapple/pull/210)). Thanks @dopry

## [0.12.0] - 2021-11-08

### Fixed

-   Fix: custom document model not working with Wagtail grapple ([#153](https://github.com/torchbox/wagtail-grapple/pull/153)). Thanks @fabienheureux
-   Fix/empty list in structblock ([#165](https://github.com/torchbox/wagtail-grapple/pull/165)). Thanks @bbliem
-   Use absolute URL for renditions ([#181](https://github.com/torchbox/wagtail-grapple/pull/181)). Thanks @fabienheureux
-   Fix channels versions solving issues introduced by Wagtail 2.14 support ([#184](https://github.com/torchbox/wagtail-grapple/pull/184)). Thanks @fabienheureux
    -   Channels can now be used with Django >= 3.x
-   Use correct endpoint url for GraphiQL when the API endpoint is on a subpath [#194](https://github.com/torchbox/wagtail-grapple/pull/194). Thanks @ruisaraiva19

### Added

-   Add contentType filter on site pages query ([#171](https://github.com/torchbox/wagtail-grapple/pull/171)). Thanks @sks
-   Add hooks for registering mutation and subscription mixins ([#155](https://github.com/torchbox/wagtail-grapple/pull/155)). Thanks @ruisaraiva19
-   Add single `GRAPPLE` setting ([#175](https://github.com/torchbox/wagtail-grapple/pull/175)). Thanks @ruisaraiva19
-   Add middleware support for queries ([#177](https://github.com/torchbox/wagtail-grapple/pull/177)). Thanks @ruisaraiva19
-   Add support for Wagtail v2.14 ([#172](https://github.com/torchbox/wagtail-grapple/pull/172)). Thanks @fabienheureux
-   Add support for Wagtail v2.15 ([#197](https://github.com/torchbox/wagtail-grapple/pull/197)). Thanks @ruisaraiva19
-   Add missing fields to images and documents ([#195](https://github.com/torchbox/wagtail-grapple/pull/195)). Thanks @ruisaraiva19

### Misc

-   Use Wagtail Sphinx theme for docs ([#183](https://github.com/torchbox/wagtail-grapple/pull/183)). Thanks @fabienheureux
-   Middleware docs updates
-   Use `blacken-docs` ([#187](https://github.com/torchbox/wagtail-grapple/pull/187))

## [0.11.0] - 2021-03-09

### Added

-   🚀 Introduced a new settings -`GRAPPLE_ALLOWED_IMAGE_FILTERS` - which accepts a list of filters (thus renditions) that are allowed to generate. Read more about generating renditions in [Wagtail docs](https://docs.wagtail.io/en/stable/advanced_topics/images/renditions.html#generating-renditions-in-python)

### Changed

-   🤖 Got deployed to PyPi automatically through the power of GitHub Actions! Yes to automation 🎉
-   📜 Changed the license from MIT to BSD 3, for better alignment with Wagtail

## [0.10.2]

### Changed

-   Allow running alongside Wagtail 2.12
-   Tweak exclusion lists for pages [#148](https://github.com/torchbox/wagtail-grapple/pull/148)

## [0.10.0]

### Added

-   Query page via url path ([#52](https://github.com/torchbox/wagtail-grapple/pull/52)). Thanks @NathHorrigan

### Fixed

-   Fix filtering by content type in page/pages queries ([#147](https://github.com/torchbox/wagtail-grapple/pull/147)). Thanks @isolationism for another PR that finally propted that fix
-   Fix "excluding custom field" warning with graphene-django>=2.8.1 ([#146](https://github.com/torchbox/wagtail-grapple/pull/146))

## [0.9.3] - 2020-12-08

-   Fix: use correct media type in GraphQLMedia [#142](https://github.com/torchbox/wagtail-grapple/pull/142)
-   Fix @register_singular_query_field usage with non-Wagtail page models did not return any result

## [0.9.2] - 2020-11-12

-   Fix a small bug for correct custom Media models support

## [0.9.1] - 2020-11-06

-   Return specific instances for `PageChooserBlock`s

## [0.9.0] - 2020-11-04

### Added

-   Support Wagtail 2.11. Further testing welcome!
-   Add collections types ([#111](https://github.com/torchbox/wagtail-grapple/pull/111)). Thanks @fabienheureux
-   Add hook for registering query mixins ([#132](https://github.com/torchbox/wagtail-grapple/pull/132)). [See documentation](https://wagtail-grapple.readthedocs.io/en/latest/general-usage/hooks.html). @zerolab
-   Add webpquality support for renditions ([#130](https://github.com/torchbox/wagtail-grapple/pull/130)). Thanks @ruisaraiva19

### Fixed

-   Fix StubModel already registered RuntimeWarning ([#133](https://github.com/torchbox/wagtail-grapple/pull/133)). @zerolab
-   Add .live().public() to all relevant methods ([#129](https://github.com/torchbox/wagtail-grapple/pull/129)). Thanks @mmmente

## [0.8.0] - 2020-10-07

### Added

-   Multi-site support - add SitesQuery and resolve pages based on site ([#115](https://github.com/torchbox/wagtail-grapple/pull/115)) Thanks @leewesleyv
-   Add GraphQLTag model ([#124](https://github.com/torchbox/wagtail-grapple/pull/124)) Thanks @ruisaraiva19
-   Add embed data for StreamField Embed blocks ([#122](https://github.com/torchbox/wagtail-grapple/pull/122))
-   Add `register_singular_query_field` decorator ([#112](https://github.com/torchbox/wagtail-grapple/pull/112))
-   Add token/slug support to register_query_field/register_paginated_query_field ([#108](https://github.com/torchbox/wagtail-grapple/pull/108))

### Fixed

-   Fix parent attribute ([#127](https://github.com/torchbox/wagtail-grapple/pull/127))
-   Fix nested StructBlock not resolving ([#118](https://github.com/torchbox/wagtail-grapple/pull/118))
-   Fix pageType returns null
-   Fix: use url instead of urlPath in redirections ([#109](https://github.com/torchbox/wagtail-grapple/pull/109)) Thanks @fabienheureux

### Misc

-   Make wagtailmedia an optional dependency ([#106](https://github.com/torchbox/wagtail-grapple/pull/106))
-   Add GraphQLPage to model types docs ([#119](https://github.com/torchbox/wagtail-grapple/pull/119)) @zerolab
-   Remove unused imports and cleanup repeat queries ([#113](https://github.com/torchbox/wagtail-grapple/pull/113))
-   Update supported versions Django (>=2.2, <3.2) and django-graphene ([#105](https://github.com/torchbox/wagtail-grapple/pull/105))

## [0.7.0] - 2020-09-02

-   Add pagination support (#101). Thanks @ruisaraiva19
-   Add contributors to README.md (#102) following the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Thanks @ruisaraiva19

## [0.6.0] - 2020-08-21

### Added

-   Add non-nullable support to `register_query_field` decorator ([#62](https://github.com/torchbox/wagtail-grapple/pull/62)). Thanks to @ruisaraiva19
-   Add `url` to `DocumentObjectType` ([#95](https://github.com/torchbox/wagtail-grapple/pull/95)). Thanks to @tbrlpld
-   Use consistent media url attributes ([#97](https://github.com/torchbox/wagtail-grapple/pull/97)). @zerolab
-   Add support for custom `Media` classes. @zerolab
-   Wheel packages are now created as well. @zerolab
-   All media (core `Image`, `Document` and [wagtailmedia](https://github.com/torchbox/wagtailmedia) `Media`) have a `url` attribute that returns the full URL to the file.
    -   The `file` attribute on `MediaObjectType` now returns the relative path. Use `url` for the full URL
    -   The `src` attribute on `BaseImageObjectType` is now deprecated in favour of `url`

### Fixed

-   Fix StructValue' object has no attribute 'value' ([#92](https://github.com/torchbox/wagtail-grapple/pull/92)). Thanks to @timmysmalls and @zerolab
-   Fix typos, update links, and lint files with pre-commit ([#91](https://github.com/torchbox/wagtail-grapple/pull/91)) Thanks to @ruisaraiva19

### Misc

-   Made Channels-related functionality optional to unblock Django 3.0.x compatibility.
    If you are using Grapple with Channels, you need to change your requirements to `wagtail_grapple[channels]`. Channels currently works only with Django 2.x

## [0.4.8] - 2019-12-14

-   Fix packaging issue that prevented installation with Wagtail 2.7

## [0.4.7] - 2019-12-14

-   Add missing migration
-   Add the base url for the embed block when needed

## [0.4.0] - 2019-12-14

-   Bump minimum python version to 3.6
-   Improve field definition and under-the-hood implementation ([#28](https://github.com/torchbox/wagtail-grapple/pull/28))
-   Add conditional checks when resolving streamfield type ([#29](https://github.com/torchbox/wagtail-grapple/pull/29))

[unreleased]: https://github.com/torchbox/wagtail-grapple/compare/v0.28.0...HEAD
[0.28.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.27.0...v0.28.0
[0.27.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.26.0...v0.27.0
[0.26.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.25.1...v0.26.0
[0.25.1]: https://github.com/torchbox/wagtail-grapple/compare/v0.25.0...v0.25.1
[0.25.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.24.0...v0.25.0
[0.24.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.23.0...v0.24.0
[0.23.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.22.0...v0.23.0
[0.22.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.21.0...v0.22.0
[0.21.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.20.0...v0.21.0
[0.20.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.19.2...v0.20.0
[0.19.2]: https://github.com/torchbox/wagtail-grapple/compare/v0.19.1...v0.19.2
[0.19.1]: https://github.com/torchbox/wagtail-grapple/compare/v0.19.0...v0.19.1
[0.19.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.18.1...v0.19.0
[0.18.1]: https://github.com/torchbox/wagtail-grapple/compare/v0.18.0...v0.18.1
[0.18.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.17.1...v0.18.0
[0.17.1]: https://github.com/torchbox/wagtail-grapple/compare/v0.17.0...v0.17.1
[0.17.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.16.0...v0.17.0
[0.16.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.15.1...v0.16.0
[0.15.1]: https://github.com/torchbox/wagtail-grapple/compare/v0.15.0...v0.15.1
[0.15.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.14.1...v0.15.0
[0.14.1]: https://github.com/torchbox/wagtail-grapple/compare/v0.14.0...v0.14.1
[0.14.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.13.0...v0.14.0
[0.13.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.12.0...v0.13.0
[0.12.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.11.0...v0.12.0
[0.11.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.10.2...v0.11.0
[0.10.2]: https://github.com/torchbox/wagtail-grapple/compare/v0.10.0...v0.10.2
[0.10.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.9.3...v0.10.0
[0.9.3]: https://github.com/torchbox/wagtail-grapple/compare/v0.9.2...v0.9.3
[0.9.2]: https://github.com/torchbox/wagtail-grapple/compare/v0.9.1...v0.9.2
[0.9.1]: https://github.com/torchbox/wagtail-grapple/compare/v0.9.0...v0.9.1
[0.9.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/torchbox/wagtail-grapple/compare/v0.4.8...v0.6.0
[0.4.8]: https://github.com/torchbox/wagtail-grapple/compare/v0.4.7...v0.4.8
[0.4.7]: https://github.com/torchbox/wagtail-grapple/compare/v0.4.0...v0.4.7
[0.4.0]: https://github.com/torchbox/wagtail-grapple/releases/tag/v0.4.0
