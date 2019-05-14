<template>
  <div id="home">
    <!-- <div
      :class="['logo', selected ? 'logo--absolute': '', ready ? 'logo--active' : '']"
      @click="closePost()"
    >
      <svg xmlns="http://www.w3.org/2000/svg" version="1" viewBox="0 0 60 60">
        <path
          d="M20.8 2.3C15.5 4 8.5 9.3 5.6 13.7c-4 5.8-5.8 14.8-4.6 21 1.2 6.7 3.3 10.8 8 15.6 15.4 16.4 43.3 9.5 49.6-12C64 19.5 49.6.7 30.2 1c-3 0-7.4.7-9.4 1.3zm15.8 6.2c20 6 22.4 32.4 4 42-1.7.7-3.2 1.3-3.3 1-.2 0 2.6-5 6.2-10.6 6.7-10.6 7.3-12.5 4.4-14.3-1.3-.7-4 .4-11.4 4.7L26.4 37c-.3 0-.2-5 .2-11.3.6-9.5.4-11.4-1-12.5-2.5-2.2-4.7 0-11 10.7C11 29.3 8 34 7.7 34c-1.3 0-1-6.5.7-11C11 16 16.8 10.3 24 8.3c5-1.4 7-1.4 12.6.3zM20.2 36c-.4 10.3.5 10.8 10 5.5 4-2 7-3.4 6.7-3l-4.5 7.7c-3.8 6.4-4.2 6.8-7 6.2-4.3-.8-11.2-5-13-8C10.8 42.3 11 42 15 35c2.3-3.8 4.5-7 4.8-7 .3 0 .4 3.6.2 8z"
        ></path>
      </svg>
    </div> -->
    <div
      :class="['post-view', selected ? 'post-view--active' : '' , ready ? 'post-view--ready' : '' ]"
    >
      <div
        class="post-view__image"
        :style="'background-image:url('+postImage+');clip-path:'+clipPath"
      ></div>
      <div class="post-view__container" v-if="selected">
        <div class="post-controls">
          <div class="post-control post-control--close" @click="closePost()">
            <i class="ion-ios-close-empty"></i>
          </div>
          <div class="post-control" id="next-post" @click="nextPost()">
            <i class="ion-ios-arrow-right"></i>
          </div>
          <div class="post-control" id="prev-post" @click="prevPost()">
            <i class="ion-ios-arrow-left"></i>
          </div>
        </div>
        <h2 class="post-view__title">{{currentPost.title}}</h2>
        <h3 class="post-view__date">{{currentPost.date}}</h3>
        <div class="post-view__content" v-html="currentPost.description"></div>
      </div>
    </div>
    <div :class="['post-list', selected ? 'post-list--hide' : '']">
      <div
        class="post"
        v-for="(item, index) in posts"
        v-on:mouseenter="changePost(index)"
        @click="selectedPost(index)"
      >
        <h2 class="post__title">
          {{item.title}}
          <span class="post__date">{{item.date}}</span>
        </h2>
      </div>
    </div>
  </div>
</template>

<script>
const posts = [
  {
    id: 1,
    title: "Wrath Analysis",
    description:
      "<p>Bespoke distillery lomo, activated charcoal sustainable pork belly art party scenester locavore. Literally typewriter asymmetrical, pork belly locavore helvetica scenester meditation squid before they sold out. Mustache celiac bespoke freegan, butcher polaroid vaporware la croix hot chicken sartorial pitchfork PBR&B. Fingerstache fashion axe polaroid, schlitz kitsch banh mi tote bag coloring book meh iPhone williamsburg squid locavore. Leggings subway tile cliche craft beer beard, cornhole lyft thundercats disrupt twee dreamcatcher sriracha chia. Williamsburg humblebrag meditation ethical disrupt authentic. YOLO sartorial subway tile squid.</p>\r\n<p>\r\nAffogato coloring book live-edge banjo letterpress brunch, chicharrones wayfarers chia asymmetrical. Gluten-free hella poutine taxidermy, put a bird on it next level twee food truck williamsburg crucifix retro chillwave humblebrag selvage subway tile. Vape trust fund fam venmo. YOLO typewriter mlkshk, leggings ennui mustache gochujang disrupt tousled. Crucifix fam lyft meggings. Austin scenester fam, iceland hammock hoodie kitsch tacos. Ramps activated charcoal tumeric, copper mug try-hard kickstarter la croix pop-up.\r\n</p>\r\n<p>\r\nPBR&B brunch iPhone whatever irony, cronut poke heirloom. Man bun leggings green juice quinoa glossier listicle activated charcoal, you probably haven't heard of them coloring book. Try-hard meggings raclette bitters fanny pack, literally lomo single-origin coffee +1 vice. Photo booth unicorn flannel umami, church-key whatever swag aesthetic cliche bushwick mixtape literally you probably haven't heard of them snackwave edison bulb. Ugh iceland jean shorts chia mixtape vexillologist. Mlkshk polaroid quinoa four dollar toast, gastropub succulents vape you probably haven't heard of them viral artisan butcher. Post-ironic put a bird on it organic microdosing, meh craft beer raclette.</p>",
    image: "https://image.ibb.co/bF9iO5/1.jpg",
    clip_path: "polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)"
  },
  {
    id: 2,
    title: "Wrath & Religion",
    description:
      "<p>Bespoke distillery lomo, activated charcoal sustainable pork belly art party scenester locavore. Literally typewriter asymmetrical, pork belly locavore helvetica scenester meditation squid before they sold out. Mustache celiac bespoke freegan, butcher polaroid vaporware la croix hot chicken sartorial pitchfork PBR&B. Fingerstache fashion axe polaroid, schlitz kitsch banh mi tote bag coloring book meh iPhone williamsburg squid locavore. Leggings subway tile cliche craft beer beard, cornhole lyft thundercats disrupt twee dreamcatcher sriracha chia. Williamsburg humblebrag meditation ethical disrupt authentic. YOLO sartorial subway tile squid.</p>\r\n<p>\r\nAffogato coloring book live-edge banjo letterpress brunch, chicharrones wayfarers chia asymmetrical. Gluten-free hella poutine taxidermy, put a bird on it next level twee food truck williamsburg crucifix retro chillwave humblebrag selvage subway tile. Vape trust fund fam venmo. YOLO typewriter mlkshk, leggings ennui mustache gochujang disrupt tousled. Crucifix fam lyft meggings. Austin scenester fam, iceland hammock hoodie kitsch tacos. Ramps activated charcoal tumeric, copper mug try-hard kickstarter la croix pop-up.\r\n</p>\r\n<p>\r\nPBR&B brunch iPhone whatever irony, cronut poke heirloom. Man bun leggings green juice quinoa glossier listicle activated charcoal, you probably haven't heard of them coloring book. Try-hard meggings raclette bitters fanny pack, literally lomo single-origin coffee +1 vice. Photo booth unicorn flannel umami, church-key whatever swag aesthetic cliche bushwick mixtape literally you probably haven't heard of them snackwave edison bulb. Ugh iceland jean shorts chia mixtape vexillologist. Mlkshk polaroid quinoa four dollar toast, gastropub succulents vape you probably haven't heard of them viral artisan butcher. Post-ironic put a bird on it organic microdosing, meh craft beer raclette.</p>",
    image: "https://image.ibb.co/dwDXGQ/2.jpg",
    // image: "./RealtimeData/religion.jpeg",
    clip_path: "polygon(31% 23%, 90% 30%, 50% 100%, 0% 50%)"
  },
  {
    id: 3,
    title: "Wrath & Voluntary",
    description:
      "<p>Bespoke distillery lomo, activated charcoal sustainable pork belly art party scenester locavore. Literally typewriter asymmetrical, pork belly locavore helvetica scenester meditation squid before they sold out. Mustache celiac bespoke freegan, butcher polaroid vaporware la croix hot chicken sartorial pitchfork PBR&B. Fingerstache fashion axe polaroid, schlitz kitsch banh mi tote bag coloring book meh iPhone williamsburg squid locavore. Leggings subway tile cliche craft beer beard, cornhole lyft thundercats disrupt twee dreamcatcher sriracha chia. Williamsburg humblebrag meditation ethical disrupt authentic. YOLO sartorial subway tile squid.</p>\r\n<p>\r\nAffogato coloring book live-edge banjo letterpress brunch, chicharrones wayfarers chia asymmetrical. Gluten-free hella poutine taxidermy, put a bird on it next level twee food truck williamsburg crucifix retro chillwave humblebrag selvage subway tile. Vape trust fund fam venmo. YOLO typewriter mlkshk, leggings ennui mustache gochujang disrupt tousled. Crucifix fam lyft meggings. Austin scenester fam, iceland hammock hoodie kitsch tacos. Ramps activated charcoal tumeric, copper mug try-hard kickstarter la croix pop-up.\r\n</p>\r\n<p>\r\nPBR&B brunch iPhone whatever irony, cronut poke heirloom. Man bun leggings green juice quinoa glossier listicle activated charcoal, you probably haven't heard of them coloring book. Try-hard meggings raclette bitters fanny pack, literally lomo single-origin coffee +1 vice. Photo booth unicorn flannel umami, church-key whatever swag aesthetic cliche bushwick mixtape literally you probably haven't heard of them snackwave edison bulb. Ugh iceland jean shorts chia mixtape vexillologist. Mlkshk polaroid quinoa four dollar toast, gastropub succulents vape you probably haven't heard of them viral artisan butcher. Post-ironic put a bird on it organic microdosing, meh craft beer raclette.</p>",
    image: "https://image.ibb.co/gnWKwQ/3.jpg",
    clip_path: "polygon(0 29%, 100% 0, 100% 70%, 48% 100%)"
  },
];
export default {
  data() {
    return {
      test: "",
      posts: posts,
      selectedClipPath: "polygon(0 100%, 0 0, 100% 0, 100% 100%)",
      postImage: posts[0].image,
      currentPost: null,
      postIndex: 0,
      selected: false,
      ready: false,
      lastSelectedPost: null,
      clipPath: posts[0].clip_path
    };
  },
  methods: {
    changePost(index) {
      if (this.postImage != this.posts[index].image && this.selected == false) {
        this.postImage = this.posts[index].image;
        this.clipPath = this.posts[index].clip_path;
      }
    },
    closePost() {
      if (this.lastSelectedPost != null) {
        this.selected = false;
        this.ready = false;
        this.clipPath = this.posts[this.lastSelectedPost].clip_path;
      }
    },
    selectedPost(index) {
      this.selected = true;
      this.clipPath = this.selectedClipPath;
      this.lastSelectedPost = index;
      this.currentPost = this.posts[index];
      setTimeout(() => {
        this.ready = true;
      }, 600);
    },
    nextPost() {
      if (this.lastSelectedPost < this.posts.length - 1) {
        this.lastSelectedPost++;
        this.ready = false;
        setTimeout(() => {
          this.currentPost = this.posts[this.lastSelectedPost];
          this.postImage = this.currentPost.image;
          this.ready = true;
        }, 600);
      }
    },
    prevPost() {
      if (
        this.lastSelectedPost <= this.posts.length - 1 &&
        this.lastSelectedPost != 0
      ) {
        this.lastSelectedPost--;
        this.ready = false;
        setTimeout(() => {
          this.currentPost = this.posts[this.lastSelectedPost];
          this.postImage = this.currentPost.image;
          this.ready = true;
        }, 600);
      }
    }
  },
  created() {
    window.addEventListener("keydown", e => {
      e.keyCode == 39 ? this.nextPost() : false;
      e.keyCode == 37 ? this.prevPost() : false;
      e.keyCode == 27 ? this.closePost() : false;
    });
  }
};
</script>




<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
$heading-font: "Nunito", sans-serif;
$body-font: "Inconsolata", monospace;
$color: #fbf9bd;
* {
  box-sizing: border-box;
}

body {
  font-family: $body-font;
}

.post {
  cursor: pointer;
  margin-bottom: 50px;
  text-align: center;
  padding: 0 40px;
  &__date {
    display: block;
    width: 100%;
    font-family: $body-font;
    font-size: 0.5em;
    margin-top: 10px;
    color: rgba(0, 0, 0, 0.5);
    font-weight: normal;
  }
  &__title {
    font-family: $heading-font;
    font-size: 2em;
    padding: 12px 30px;
    font-weight: bold;
    position: relative;
    &:after {
      position: absolute;
      left: 0;
      top: 0;
      height: 100%;
      width: 0;
      z-index: -1;
      transition: width 0.3s ease 0s;
      content: "";
      background: $color;
      transform: skew(-20deg);
    }
    &:hover:after {
      width: 100%;
    }
  }
  &:last-child {
    margin-bottom: 0;
  }
}

.post-list {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  padding: 30px 0;
  flex-wrap: wrap;
  flex-direction: column;
  align-items: center;
  position: relative;
  transition: all 0.3s ease 0s;
  transform: translateY(0px);
  visibility: visible;
  &--hide {
    transform: translateY(-20px);
    opacity: 0;
    visibility: hidden;
  }
}

.post-view {
  transition: 0.3s ease 0s;
  width: 100%;
  min-height: 100vh;
  position: absolute;
  left: 0;
  top: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  &__date {
    font-family: $body-font;
    margin-bottom: 60px;
    transform: translateY(45px);
    transition: transform 0.3s ease 0s;
  }
  &__image {
    position: fixed;
    transition: all 0.5s ease 0s;
    clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
    width: 800px;
    background-size: cover;
    background-position: top;
    overflow: hidden;
    height: 450px;
    top: 50%;
    margin-top: -225px;
  }
  &__container {
    position: absolute;
    top: 100px;
    width: 100%;
    max-width: 900px;
    z-index: 99;
    opacity: 0;
    transition: all 0.3s ease 0s;
  }
  &__content {
    background: #fff;
    padding: 40px;
    margin-bottom: 80px;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
    transform: translateY(85px);
    transition: transform 0.3s ease 0s;
    p {
      font-size: 1.125em;
      margin-bottom: 30px;
      line-height: 25px;
      &:last-child {
        margin-bottom: 0;
      }
    }
  }
  &--active {
    .post-view__image {
      background-position: top;
      transition: all 0.6s ease 0s;
      width: 100%;
      height: 520px;
      margin-top: 0;
      top: 0;
    }
  }
  &__title {
    font-size: 2.875em;
    font-weight: bold;
    font-family: $heading-font;
    margin: 30px 0 15px 0;
    transform: translateY(45px) scaleY(0);
    transition: transform 0.3s ease-out 0s;
  }
  &--ready {
    .post-view {
      &__container {
        opacity: 1;
      }
      &__date,
      &__content {
        transform: translateY(0px);
      }
      &__title {
        transform: translateY(0px) scaleY(1);
      }
    }
  }
}

.post-controls {
  position: fixed;
  right: 20px;
  flex-direction: column;
  top: 20px;
  display: flex;
}

.post-control {
  cursor: pointer;
  font-size: 1.375em;
  background: $color;
  margin-bottom: 15px;
  height: 40px;
  width: 40px;
  border-radius: 50%;
  text-align: center;
  line-height: 43px;
  transition: all 0.3s ease 0s;
  &:hover {
    box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
  }
  &--close {
    font-size: 2em;
    background: rgba(#000, 0.3);
    color: #fff;
    &:hover {
      background: #000;
    }
  }
}

@media only screen and (max-width: 991px) {
  html {
    font-size: 13px;
  }
  .post-controls {
    bottom: 10px;
    z-index: 99;
    top: auto;
    background: rgba(#000, 0.7);
    padding: 0 5px;
    justify-content: center;
    margin: auto;
    border-radius: 30px;
    height: 55px;
    align-items: center;
    flex-direction: row-reverse;
  }
  .post-control {
    margin: 0 5px;
    &--close {
      background: #000;
    }
  }
  .post-view__container {
    padding: 0 30px;
  }
}

.logo {
  cursor: pointer;
  position: fixed;
  left: 30px;
  top: 30px;
  z-index: 9;
  width: 50px;
  height: 50px;
  transition: 0.3s ease 0s;
  &--absolute {
    position: absolute;
    svg {
      fill: $color;
    }
  }
  &--active {
    svg {
      fill: #fff;
    }
  }
  svg {
    width: 100%;
    transition: all 0.3s ease 0s;
  }
}
</style>
