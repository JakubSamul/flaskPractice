<template>
    <div class="spaceBackground" />
</template>
<script>
export default {
  name: 'BackGround',
};
</script>
<style lang="scss" scoped>
.spaceBackground {
    position: fixed;
    top: 0;
    z-index: -1;
    width: 100%;
    height: 100vh;
    background-image: url('../assets/background.jpg');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: 80% 0%;
}
</style>
