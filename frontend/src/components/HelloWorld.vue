<template>
  <v-container class="fill-height" max-width="900">
    <div>
      <v-img
        class="mb-4"
        height="150"
        src="@/assets/logo.png"
      />

      <div class="mb-8 text-center">
        <div class="text-body-2 font-weight-light mb-n1">Welcome to</div>
        <h1 class="text-h2 font-weight-bold">Vuetify</h1>
      </div>
      <v-row>
        <v-col>
          <v-card
            class="py-4 text-center"
            :href="dummyViewUrl"
            :loading="dummyViewLoading"
            target="_blank"
            :text="dummyViewText"
            title="Dummy View"
            variant="tonal"
          />
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
        <v-col cols="12">
          <v-card
            class="py-4 text-center"
            :loading="dummyWebsocketLoading"
            :text="dummyWebsocketText"
            title="Dummy Websocket"
            variant="tonal"
          />
        </v-col>
        <v-col cols="auto">
          <v-number-input v-model="dummyWebsocketPK" hide-details label="PK" :min="1" />
        </v-col>
        <v-col cols="auto">
          <v-btn @click="wsSend">Retrieve</v-btn>
        </v-col>

      </v-row>
      <v-row>
        <v-col cols="12">
          <v-card
            class="py-4"
            color="surface-variant"
            image="https://cdn.vuetifyjs.com/docs/images/one/create/feature.png"
            prepend-icon="mdi-rocket-launch-outline"
            rounded="lg"
            variant="tonal"
          >
            <template #image>
              <v-img position="top right" />
            </template>

            <template #title>
              <h2 class="text-h5 font-weight-bold">
                Get started
              </h2>
            </template>

            <template #subtitle>
              <div class="text-subtitle-1">
                Change this page by updating <v-kbd>{{ `<HelloWorld />` }}</v-kbd> in <v-kbd>components/HelloWorld.vue</v-kbd>.
              </div>
            </template>
          </v-card>
        </v-col>

        <v-col v-for="link in links" :key="link.href" cols="6">
          <v-card
            append-icon="mdi-open-in-new"
            class="py-4"
            color="surface-variant"
            :href="link.href"
            :prepend-icon="link.icon"
            rel="noopener noreferrer"
            rounded="lg"
            :subtitle="link.subtitle"
            target="_blank"
            :title="link.title"
            variant="tonal"
          />
        </v-col>
      </v-row>

    </div>
  </v-container>
</template>

<script setup lang="ts">
  const links = [
    {
      href: 'https://vuetifyjs.com/',
      icon: 'mdi-text-box-outline',
      subtitle: 'Learn about all things Vuetify in our documentation.',
      title: 'Documentation',
    },
    {
      href: 'https://vuetifyjs.com/introduction/why-vuetify/#feature-guides',
      icon: 'mdi-star-circle-outline',
      subtitle: 'Explore available framework Features.',
      title: 'Features',
    },
    {
      href: 'https://vuetifyjs.com/components/all',
      icon: 'mdi-widgets-outline',
      subtitle: 'Discover components in the API Explorer.',
      title: 'Components',
    },
    {
      href: 'https://discord.vuetifyjs.com',
      icon: 'mdi-account-group-outline',
      subtitle: 'Connect with Vuetify developers.',
      title: 'Community',
    },
  ]

  const dummyViewUrl = 'http://127.0.0.1:8000/';
  const dummyViewText = ref('Loading');
  const dummyViewLoading = ref(true);
  // TODO: Better use useFetch for this
  fetch(dummyViewUrl)
    .then(response => response.text())
    .then(async text => {
      await new Promise(r => setTimeout(r, 1000))
      return text;
    })
    .then(text => {
      dummyViewText.value = text;
    }).catch(e => {
      dummyViewText.value = `Something went wrong\n${e}`
    }).finally(() => {
      dummyViewLoading.value = false;
    });


  const dummyWebsocketUrl = 'ws://127.0.0.1:8000/ws/';
  const dummyWebsocketText = ref('Loading');
  const dummyWebsocketLoading = ref(true);
  const dummyWebsocketPK = ref(1);
  const dummyWebsocket = new WebSocket(dummyWebsocketUrl);
  dummyWebsocket.onopen = (e) => {
    dummyWebsocketLoading.value = false;
    dummyWebsocketText.value = `Ready\n${JSON.stringify(e)}`;
  };
  dummyWebsocket.onmessage = (e) => {
    dummyWebsocketText.value = `Message\n${e.data}`;
  }
  dummyWebsocket.onerror = (e) => {
    dummyWebsocketText.value = `Error\n${JSON.stringify(e)}`;
  }
  dummyWebsocket.onclose = (e) => {
    dummyWebsocketText.value = `Closed\n${JSON.stringify(e)}`;
  }
  function wsSend(): void {
    if (dummyWebsocket.readyState != dummyWebsocket.OPEN) return;
    dummyWebsocket.send(JSON.stringify({
      action: 'retrieve',
      request_id: new Date().getTime(),
      pk: dummyWebsocketPK.value,
    }));
  }

</script>
