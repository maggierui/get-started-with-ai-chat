import type { JSX } from "react";
import {
  Button,
  Drawer,
  DrawerBody,
  DrawerHeader,
  DrawerHeaderTitle,
  Subtitle2,
  Switch,
} from "@fluentui/react-components";
import { Dismiss24Regular } from "@fluentui/react-icons";

import styles from "./SettingsPanel.module.css";
import { ThemePicker } from "./theme/ThemePicker";

export interface ISettingsPanelProps {
  isOpen: boolean;
  onOpenChange: (isOpen: boolean) => void;
  useMetadataInference: boolean;
  onUseMetadataInferenceChange: (useInference: boolean) => void;
}

export function SettingsPanel({
  isOpen = false,
  onOpenChange,
  useMetadataInference,
  onUseMetadataInferenceChange,
}: ISettingsPanelProps): JSX.Element {
  return (
    <Drawer
      className={styles.panel}
      onOpenChange={(_, { open }) => {
        onOpenChange(open);
      }}
      open={isOpen}
      position="end"
    >
      <DrawerHeader>
        <DrawerHeaderTitle
          action={
            <div>
              <Button
                appearance="subtle"
                icon={<Dismiss24Regular />}
                onClick={() => {
                  onOpenChange(false);
                }}
              />
            </div>
          }
        >
          Settings
        </DrawerHeaderTitle>
      </DrawerHeader>{" "}
      <DrawerBody className={styles.content}>
        <div className={styles.section}>
          <Subtitle2>Retrieval</Subtitle2>
          <div className={styles.row}>
            <Switch
              checked={useMetadataInference}
              label="Metadata inference"
              onChange={(_, data) => onUseMetadataInferenceChange(Boolean(data.checked))}
            />
            <div className={styles.caption}>
              Toggle on to allow the backend to use inferred metadata hints; off to keep natural retrieval.
            </div>
          </div>
        </div>
        <ThemePicker />
      </DrawerBody>
    </Drawer>
  );
}
