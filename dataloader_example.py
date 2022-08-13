from typing import Dict

import yaml

from dataset.dota import DoTADataset


def load_yaml(yaml_file: str) -> Dict:
    """
    Load yaml file.
    """
    with open(yaml_file) as stream:
        param = yaml.safe_load(stream)
    return param


def main():

    config = load_yaml("config/config_example.yaml")
    phase = "train"
    dota_dataset = DoTADataset(config=config, phase=phase)
    print("beautiful world")

    for i, (
        input_bbox,
        input_flow,
        input_ego_motion,
        target_bbox,
        target_ego_motion,
    ) in enumerate(dota_dataset):

        print(f"{phase} dataset length: {len(dota_dataset)}")

        print(f"loop {i+1}")
        print(f"input_bbox: {input_bbox.shape}")
        print(f"input_flow: {input_flow.shape}")
        print(f"input_ego_motion: {input_ego_motion.shape}")
        print(f"target_bbox: {target_bbox.shape}")
        print(f"input_bbox: {target_ego_motion.shape}")

        break  # for debug


if __name__ == "__main__":
    main()
