import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { IThemeManager } from '@jupyterlab/apputils';

/**
 * Initialization data for the jupyterlab_theme_light_minimal extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab_theme_light_minimal:plugin',
  autoStart: true,
  requires: [IThemeManager],
  activate: (app: JupyterFrontEnd, manager: IThemeManager) => {
    console.log('JupyterLab extension jupyterlab_theme_light_minimal is activated!');
    const style = 'jupyterlab_theme_light_minimal/index.css';

    manager.register({
      name: 'jupyterlab_theme_light_minimal',
      isLight: true,
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve(undefined)
    });
  }
};

export default plugin;
