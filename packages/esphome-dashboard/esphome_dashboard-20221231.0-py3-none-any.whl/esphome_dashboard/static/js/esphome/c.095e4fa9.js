import{b as o,d as t,n as e,s as i,y as n,$ as s,j as a}from"./index-862daf1e.js";import"./c.cd48e96a.js";import"./c.4b1d9c02.js";let c=class extends i{render(){return n`
      <esphome-process-dialog
        .heading=${`Clean ${this.configuration}`}
        .type=${"clean"}
        .spawnParams=${{configuration:this.configuration}}
        @closed=${this._handleClose}
      >
        <mwc-button
          slot="secondaryAction"
          dialogAction="close"
          label="Edit"
          @click=${this._openEdit}
        ></mwc-button>
        <mwc-button
          slot="secondaryAction"
          dialogAction="close"
          label="Install"
          @click=${this._openInstall}
        ></mwc-button>
      </esphome-process-dialog>
    `}_openEdit(){s(this.configuration)}_openInstall(){a(this.configuration)}_handleClose(){this.parentNode.removeChild(this)}};o([t()],c.prototype,"configuration",void 0),c=o([e("esphome-clean-dialog")],c);
