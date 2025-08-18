# Requirements: pip install matplotlib matplotlib-venn
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles

def shade_regions(ax, regions):
    # Draw a generic 3-set Venn with all regions present
    v = venn3(subsets=(1,1,1,1,1,1,1), set_labels=('A','B','C'), ax=ax)

    # Clear subset labels safely: subset_labels is a list indexed by 0..6
    if v.subset_labels:
        for i, lbl in enumerate(v.subset_labels):
            if lbl is not None:
                lbl.set_text('')

    # Light base color for all present patches
    for area_key in ['100','010','001','110','101','011','111']:
        patch = v.get_patch_by_id(area_key)
        if patch is not None:
            patch.set_alpha(0.2)
            patch.set_color('#cccccc')

    # Emphasize the target regions
    for area_key in regions:
        patch = v.get_patch_by_id(area_key)
        if patch is not None:
            patch.set_alpha(0.8)
            patch.set_color('#4e79a7')

    venn3_circles(subsets=(1,1,1,1,1,1,1), ax=ax)

# Mapping of region IDs:
# '100': A only, '010': B only, '001': C only
# '110': A∩B only, '101': A∩C only, '011': B∩C only, '111': A∩B∩C

fig, axes = plt.subplots(2, 2, figsize=(10, 9))
fig.suptitle('Distributive Laws via Venn Diagrams', fontsize=16)

# Law 1 LHS: A ∩ (B ∪ C) -> 110,101,111
shade_regions(axes[0,0], regions=['110','101','111'])
axes[0,0].set_title('LHS: A ∩ (B ∪ C)')

# Law 1 RHS: (A ∩ B) ∪ (A ∩ C) -> 110,101,111
shade_regions(axes[0,1], regions=['110','101','111'])
axes[0,1].set_title('RHS: (A ∩ B) ∪ (A ∩ C)')

# Law 2 LHS: A ∪ (B ∩ C) -> 100,110,101,111,011
shade_regions(axes[1,0], regions=['100','110','101','111','011'])
axes[1,0].set_title('LHS: A ∪ (B ∩ C)')

# Law 2 RHS: (A ∪ B) ∩ (A ∪ C) -> 100,110,101,111,011
shade_regions(axes[1,1], regions=['100','110','101','111','011'])
axes[1,1].set_title('RHS: (A ∪ B) ∩ (A ∪ C)')

for ax in axes.ravel():
    ax.set_axis_off()

plt.tight_layout()
plt.show()
