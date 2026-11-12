# Learning/reference map

- [Preview](learning-map.svg): a static map of the source inventory, not a runtime architecture or completion badge.
- [Editable source](learning-map.excalidraw): download and open using Excalidraw's **Open** action, or import into a compatible local editor. Each label, box, and arrow is a native editable element; no flattened image, private paths, credentials, or personal activity data is embedded.

The book/source collection is external. Local guides and references support study; the dashed practice box marks resources mentioned by the guides but absent from the original tracked snapshot. Arrows mean suggested reading order, not code dependencies, copied-code lineage, authorship, or completed exercises. See the root [README](../README.md) for provenance, credits, rights uncertainty, and the exact inventory revision.

## Updating the diagram

1. Edit the native elements in `learning-map.excalidraw` and save the file here.
2. Regenerate the matching SVG using the standard-library-only documentation utility:

   ```bash
   python3 docs/render_learning_map.py
   ```

3. Check the saved preview is current:

   ```bash
   python3 docs/render_learning_map.py --check
   git diff --check
   ```

These are documentation-rendering/validation commands, not application setup, builds, or exercise tests. The renderer supports this map's unrotated rectangles, plain text, and straight arrows only; if editing introduces unsupported elements, it fails instead of silently omitting them. Preview regeneration does not run any embedded Python examples. Inspect the SVG after editing for readability and placement. The SVG uses a white canvas and dark ink for standalone GitHub/image viewing; it is not the editable source.

Do not label a future exercise as complete until its source, changes from upstream, applicable notices, and actual validation evidence are available. Keep book/upstream, verified human, and documented AI assistance credits separate.
