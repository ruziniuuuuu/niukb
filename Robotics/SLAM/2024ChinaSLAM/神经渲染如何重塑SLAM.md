# 神经渲染如何重塑SLAM

## TODO

- [ ] octree

## Neural rendering

Pose estimation as pre-processing

camera pose始终已知，但在SLAM里并没有一个初始的位姿。

## SLAM

- Classical sparse visual SLAM
  - sparse: ORB-SLAM
    - multi-map sparse points
    - work on an active map
    - local mapping thread,
    - oop and map merging thread
    - adv:
      - fast
      - loop closure
      - global BA
    - disa:
      - sparse point cloud
    - so we need some dense representation
  - Dense visual SLAM: DROID-SLAM
    - consistent 3D representation
    - loop closure + full BA

## RGB-D SLAM

- iMAP
  - Nerf-based SLAM
  - secne rep: implicit surface based on MLP, dense, 3D consistent
  - method:
    - tracking: parallel tracking process
    - mapping
  - challenge: slow
    - solution:
      - keyframe selection
      - active sampling
- NICE-SLAM
  - scene rep: multi-resolution feature grid + small MLP
  - comparison with iMAP: map rep saces local info, higher quality ans faster convergence
- other map rep:
  - Vox fusion: Octree + MLP
  - Co-SLAM: Hash-grid + MLP
  - ESLAM: Triplane + MLP
  - Point-SLAM: points + MLP
- 3DGS-based scene rep:
  - works:
    - GaussianSLAM
    - GS-SLAM
    - SplaTAM
    - Photo-SLAM
  - Full image redering loss (in contrast to sparsely sampling pixels in NeRF-based)
  - challenges compared to NeRF-based
    - Gaussian insertion
      - solution: GaussianSLAM, GS-SLAM, SplaTAM
    - lack of inductive bias
      - solution: GaussianSLAM
  - Comparisons of different methods: ref to the survey
    - How Nerfs and 3DGS are reshaping SLAM: A survey
    - results:
      - mapping: good!
      - tracking: worse than traditional method

How is iMAP different from tradition?

- map rep
- trackig: frame-to-frame vs. frame-to-model
- loss func
- loop closure & global BA
  - not supported by iMAP

How to incorporate loop closure and global BA?

- GO-SLAM
  - DBA optimizes supervision of map training, but how about efficient mao update?
- NGEL-SLAM: how ro quickly adjust neural map after loop closure?
  - use **sub-maps** to quickly update after pose updates due to loop closure
  - adv:
    - explicit LP and glocal BA
    - global consistent
    - GPU-based, in parallel, low latency
    - Dense mapping (Mesh)
  - other sub-map based: ...

## RGB-based

Nerf:

- DIM-SLAM: warping loss
  - warping loass
  - patch-wise SSIM loss
- NICER-SLAM: Monocular depth
  - use mono depth as supervision
- ${\niu (v)}DBA $: Neural implicit dense BA
  - supervisde by optical floa
  - Neural implicit surface
  - dense BA
  - Ablation study
    - photometric loss increases completeness, but increasly decrease accuracy
    - could be due to illumination disturbance
    - advs:
      - self-supervised optical flow

3D GS:

- GSSLAM
  - photometric loss
  - Gaussian initialization
  - Clear gap between RGB and RGB-D versions
- PhotoSLAM
  - ORB3 as tracking and sparse 3D points (geo loss)
  - loop closure is considered
  - Gaussian den
- mapping: Clear gap between RGB-D and RGB
- tracking: similar

## More sensors and applications

- Event-camera SLAM
  - Event and RDB-D as input
  - Robust performance in motion blurred and dark seqs
- Lidar SLAM
  - Octree + MLP
- Semantic SLAM
  - iLabel
  - SNI-SLAM
- Dynamic SLAM
  - semantic segmentation and motion estimation
  - 4D rep

## Conclusion

How does NeRF/3DGS reshape SLAM?

- sparse point map / inconsistent 3D rep -> dense & consistent map
- tradion: advs in LC and BA
- form of supervision is important
- global consistent and low latency NeRF

NeRF vs SLAM
